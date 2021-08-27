from matrixOperations import *


def generateProjMat(thetas):
    thetaX, thetaY, thetaZ = [thetas[i] for i in ['thetaX', 'thetaY', 'thetaZ']]

    xRotationMatrix, yRotationMatrix, zRotationMatrix = rotationInX(thetaX), rotationInY(thetaY), rotationInZ(thetaZ)
    ortho_matrix = orthoMatrix()
    finalMatrix = ProjectionMatrix(combineMatrices(xRotationMatrix, yRotationMatrix, zRotationMatrix, ortho_matrix))
    return finalMatrix


def identityMat():
    idMat = ProjectionMatrix(matrix=[
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])
    return idMat


def orthoMatrix():
    ortho_matrix = ProjectionMatrix(matrix=[
        [1, 0, 0],
        [0, 1, 0],
    ])
    return ortho_matrix


def rotationInX(thetaX):
    rotationX = ProjectionMatrix(matrix=[
        [1, 0, 0],
        [0, math.cos(thetaX), -math.sin(thetaX)],
        [0, math.sin(thetaX), math.cos(thetaX)],
    ])

    return rotationX

def rotationInY(thetaY):
    rotationY = ProjectionMatrix(matrix=[
        [math.cos(thetaY), 0, -math.sin(thetaY)],
        [0, 1, 0],
        [math.sin(thetaY), 0, math.cos(thetaY)],
    ])

    return rotationY


def rotationInZ(thetaZ):
    rotationZ = ProjectionMatrix(matrix=[
        [math.cos(thetaZ), -math.sin(thetaZ), 0],
        [math.sin(thetaZ), math.cos(thetaZ), 0],
        [0, 0, 1],
    ])
    return rotationZ




