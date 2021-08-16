from  kernel import  kernel
import numpy as np
from tqdm import tqdm

class matchProvider:
    def __init__(self, numOfRowKernel, numOfColumnKernel, anchorLocationRow, anchorLocationCol, leftImage, rightImage, disparity):
        self.numOfRowsOfKernel = numOfRowKernel
        self.numOfColumnOfKernel = numOfColumnKernel
        self.anchorLocationRow = anchorLocationRow
        self.anchorLocationCol = anchorLocationCol
        self.disparity = disparity
        self.matchingKernel = kernel(numOfRowKernel, numOfColumnKernel, anchorLocationRow, anchorLocationCol)
        self.leftImage = leftImage
        self.rightImage = rightImage
        [self.numOfRowsImage , self.numOfColsImage] = self.leftImage.shape
        self.minMaxLeft = []
        self.minMaxRight = []

        tempRowOfDic = []
        for col in range(self.numOfColsImage):
            tempRowOfDic.append(dict({"minIndex":[-1,-1] , "maxIndex":[-1,-1]}))
        for row in range(self.numOfRowsImage):
            self.minMaxLeft.append(tempRowOfDic.copy())
            self.minMaxRight.append(tempRowOfDic.copy())
        self.result = np.zeros([self.numOfRowsImage , self.numOfColsImage])
    def match(self):
        for row in tqdm(range(self.anchorLocationRow,self.numOfRowsImage-self.numOfRowsOfKernel+self.anchorLocationRow)):
            for col in range(self.anchorLocationCol,self.numOfColsImage-self.numOfColumnOfKernel+self.anchorLocationCol-self.disparity):
                self.minMaxRight[row][col] = self.matchingKernel.findMinMaxIndexsInKernel(self.rightImage, row, col)
                self.minMaxLeft[row][col] = self.matchingKernel.findMinMaxIndexsInKernel(self.leftImage, row, col + self.disparity)
        for row in tqdm(range(self.anchorLocationRow,self.numOfRowsImage-self.numOfRowsOfKernel+self.anchorLocationRow)):
            for col in range(self.anchorLocationCol,self.numOfColsImage-self.numOfColumnOfKernel+self.anchorLocationCol-self.disparity):
                if (self.minMaxRight[row][col]['minIndex']==self.minMaxLeft[row][col]['minIndex']) \
                        and self.minMaxRight[row][col]['minIndex']!=[-self.matchingKernel.anchorLocationRow,-self.matchingKernel.anchorLocationRow]\
                        and self.minMaxRight[row][col]['maxIndex']!=[-self.matchingKernel.anchorLocationRow,-self.matchingKernel.anchorLocationRow]\
                        and (self.minMaxRight[row][col]['maxIndex']==self.minMaxLeft[row][col]['maxIndex']):
                    self.result[row][col] = 255


        return self.result

