from listModification import *
from linearAlgebra.specialMatrices import *

from rendererWorkStation.schematicLab import *

from display import *


def schemToStrokes(schematic):
    strokes = []

    thetas = updateRotation(rendererMainData.angleRotationRates)
    multMatrix = matricesData.rotationProjMat(thetas)
    strokes = [schemSetToStrokes(schemSet, multMatrix) for schemSet in schematic]

    return strokes


def schemSetToStrokes(schemSet, multMatrix):
    geometry = doProjections(multMatrix, schemSet['points'], schemSet['lines'], schemSet['triangles'])
    points, lines, triangles = [geometry[i] for i in ['points', 'lines', 'triangles']]

    drawingDict = allCoordConversions(points, lines, triangles)
    drawingDict['color'] = schemSet['color']
    drawingDict['point size'] = schemSet['point size']

    return drawingDict


def doProjections(multMatrix, points, lines, triangles):
    if points: points = projectFeatures(multMatrix, points)
    if lines: lines = projectFeatures(multMatrix, lines)
    if triangles: triangles = projectFeatures(multMatrix, triangles)
    return {'points': points, 'lines': lines, 'triangles': triangles}


def projectFeatures(multMatrix, features):
    featureSize = len(features[0])
    featuresMatrix = findTranspose(ungroupListElements(features))
    projectedFeatures = np.dot(multMatrix, featuresMatrix)
    features = groupListElements(findTranspose(projectedFeatures), groupSize=featureSize)
    return features


def allCoordConversions(points, lines, triangles):
    windowSetObj = windowTracker.windowSetObj
    allPointPixels = [[windowSetObj.coordsToPixel(point[i]) for i in range(len(point))] for point in points]
    allLinePixels = [[windowSetObj.coordsToPixel(line[i]) for i in range(len(line))] for line in lines]
    allTrianglePixels = [[windowSetObj.coordsToPixel(triangle[i]) for i in range(len(triangle))] for triangle in triangles]

    drawingDict = {'points': allPointPixels, 'lines': allLinePixels, 'triangles': allTrianglePixels}
    return drawingDict











