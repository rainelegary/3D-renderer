sys = __import__("sys")  # import sys
math = __import__("math")  # import math
from globalVars import *

class ProjectionMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.numCols = len(self.matrix[0])
        self.numRows = len(self.matrix)


    def projVec(self, inVec=()):
        numCols = self.numCols
        if numCols != len(inVec):
            print(self.matrix)
            print(inVec)
            sys.exit("Incompatible vector given in ProjectionMatrix >> projVec")

        rowNum = 0
        pVec = []
        for row in self.matrix:
            pVecEntry = 0
            for colNum in range(numCols):
                pVecEntry += row[colNum] * inVec[colNum]

            pVec.append(pVecEntry)
            rowNum += 1

        return tuple(pVec)


    def matMul(self, otherMatrix=(), ownOnLeft=True):
        ownMatrix = self.matrix
        if ownOnLeft:
            leftMatrix = ownMatrix
            rightMatrix = otherMatrix
        else:
            leftMatrix = otherMatrix
            rightMatrix = ownMatrix

        leftRowCount = len(leftMatrix)
        leftColCount = len(leftMatrix[0])
        rightRowCount = len(rightMatrix)
        rightColCount = len(rightMatrix[0])

        resultingMat = []
        for resRowNum in range(leftRowCount):
            resultingMatRow = []
            for resColNum in range(rightColCount):
                resEntry = 0
                # if leftColCount != rightRowCount:
                #     sys.exit("incompatible matrix sizes in ProjectionMatrix >> matMul")
                for entryNum in range(rightRowCount):
                    resEntry += leftMatrix[resRowNum][entryNum] * rightMatrix[entryNum][resColNum]

                resultingMatRow.append(resEntry)
            resultingMat.append(resultingMatRow)

        return resultingMat


def combineMatrices(*matrixList):

    recentMatrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

    for matrix in matrixList:
        recentMatrix = matrix.matMul(recentMatrix)

    return recentMatrix


def findTranspose(matrix):

    tEntries = []
    for col in range(len(matrix[0])):

        tRow = []
        for row in matrix:
            tRow.append(row[col])
        tEntries.append(tRow)

    return tEntries

