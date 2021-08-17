from matplotlib import pyplot as plt
from matchProvider import matchProvider
from tqdm import tqdm
import numpy as np
import cv2


# leftImage = cv2.imread('../cutSSDByPython/leftPic.png', 0)
# rightImage = cv2.imread('../cutSSDByPython/rightPic.png', 0)
leftImage = cv2.imread('/home/farshad/Desktop/drivingStereo_left/2018-07-09-16-11-56_2018-07-09-16-12-06-408.jpg', 0)
rightImage = cv2.imread('/home/farshad/Desktop/drivingStereo_right/2018-07-09-16-11-56_2018-07-09-16-12-06-408.jpg', 0)
originalImageShape = (leftImage.shape[1],leftImage.shape[0])

scale_percent = 60 # percent of original size
width = int(leftImage.shape[1] * scale_percent / 100)
height = int(leftImage.shape[0] * scale_percent / 100)
dim = (width, height)
leftImage = cv2.resize(leftImage, dim, interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, dim, interpolation = cv2.INTER_AREA)
# cv2.imshow("testRight",rightImage)
# cv2.imshow("testLeft",leftImage)
# cv2.waitKey(0)

selectedDisparity = int(20*scale_percent/100)


minMaxMatchProvider_upToDown = matchProvider(numOfRowKernel = 5, numOfColumnKernel = 1, anchorLocationRow =0, anchorLocationCol= 0 , leftImage = leftImage, rightImage = rightImage, disparity =selectedDisparity)
result_upToDown = minMaxMatchProvider_upToDown.match()
minMaxMatchProvider_downToUp = matchProvider(numOfRowKernel = 5, numOfColumnKernel = 1, anchorLocationRow =2, anchorLocationCol= 0 , leftImage = leftImage, rightImage = rightImage, disparity =selectedDisparity)
result_downToUp = minMaxMatchProvider_downToUp.match()

minMaxMatchProvider_leftToRight = matchProvider(numOfRowKernel = 1, numOfColumnKernel = 5, anchorLocationRow =0, anchorLocationCol= 0 , leftImage = leftImage, rightImage = rightImage, disparity =selectedDisparity)
result_leftToRight = minMaxMatchProvider_leftToRight.match()
minMaxMatchProvider_rightToLeft = matchProvider(numOfRowKernel = 1, numOfColumnKernel = 5, anchorLocationRow =0, anchorLocationCol= 2 , leftImage = leftImage, rightImage = rightImage, disparity =selectedDisparity)
result_rightToLeft= minMaxMatchProvider_rightToLeft.match()



numOfRow, numOfCol = result_upToDown.shape
print(result_upToDown.shape)
result_total = np.zeros([numOfRow ,numOfCol])
for row in range(numOfRow):
    for col in range(numOfCol):
        if result_upToDown[row][col]+  result_downToUp[row][col] + result_leftToRight[row][col]+ result_rightToLeft[row][col]>=3*255 :
            result_total[row][col] = 255
        else:
            result_total[row][col] = 0

result_total = cv2.resize(result_total, originalImageShape, interpolation = cv2.INTER_AREA)
plt.imsave("results/resultHierarchySize{}.png".format(scale_percent),result_total)
plt.imshow(result_total)
plt.show()
