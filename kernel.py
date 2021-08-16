from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm
class kernel:
    def __init__(self, numOfRow, numOfColumn, anchorLocationRow, anchorLocationCol):
        self.numOfRowsOfKernel = numOfRow
        self.numOfColumnOfKernel = numOfColumn
        self.anchorLocationRow = anchorLocationRow
        self.anchorLocationCol = anchorLocationCol

    def findMinMaxIndexsInKernel(self, image, locationRow, locationCol):
        minIntensity = 256
        maxIntensity = -1
        minIndexes = [0,0]
        maxIndexes = [0,0]
        for row in range(self.numOfRowsOfKernel):
            for col in range(self.numOfColumnOfKernel):
                if minIntensity > int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol]):
                    minIntensity = int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol])
                    minIndexes[0] = row - self.anchorLocationRow
                    minIndexes[1] = col - self.anchorLocationCol
                if maxIntensity < int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol]):
                    maxIntensity = int(image[row + locationRow - self.anchorLocationRow][col + locationCol - self.anchorLocationCol])
                    maxIndexes[0] = row - self.anchorLocationRow
                    maxIndexes[1] = col - self.anchorLocationCol
        result = dict({"minIndex":minIndexes , "maxIndex":maxIndexes})
        return  result


