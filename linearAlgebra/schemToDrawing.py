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
    features = schemSet['features']
    geometry = doProjections(multMatrix, features['points'], features['lines'], features['triangles'])
    points, lines, triangles = [geometry[i] for i in ['points', 'lines', 'triangles']]

    features = allCoordConversions(points, lines, triangles)
    drawingDict = {}
    drawingDict['features'] = features
    drawingDict['colors'] = schemSet['colors']
    drawingDict['set specs'] = schemSet['set specs']

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

    features = {'points': allPointPixels, 'lines': allLinePixels, 'triangles': allTrianglePixels}
    return features











