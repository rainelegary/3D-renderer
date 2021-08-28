sys = __import__("sys")  # import sys
math = __import__("math")  # import math
import numpy as np

from varStorage import *


def combineMatrices(*matrixList):

    recentMatrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]

    for matrix in matrixList:
        recentMatrix = np.dot(matrix, recentMatrix)

    return recentMatrix


def findTranspose(matrix):

    tEntries = []
    for col in range(len(matrix[0])):

        tRow = []
        for row in matrix:
            tRow.append(row[col])
        tEntries.append(tRow)

    return tEntries

