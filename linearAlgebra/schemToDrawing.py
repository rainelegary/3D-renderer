from listModification import *
from linearAlgebra.specialMatrices import *

from rendererWorkStation.schematicLab import *

from display import *


def schemToStrokes(schematic):
    strokes = []

    thetaSpeeds = rendererMainData.angleRotationRates
    thetas = updateRotation(thetaSpeeds)
    multMatrix = matricesData.rotationProjMat(thetas)

    for schemSet in schematic:
        points, lines, triangles = schemSet['points'], schemSet['lines'], schemSet['triangles']

        geometry = doProjections(multMatrix, points, lines, triangles)
        points, lines, triangles = [geometry[i] for i in ['points', 'lines', 'triangles']]

        drawingDict = allCoordConversions(points, lines, triangles)

        drawingDict['color'] = schemSet['color']
        drawingDict['point size'] = schemSet['point size']

        strokes.append(drawingDict)

    return strokes



def doProjections(multMatrix, points, lines, triangles):
    if points:
        points = projectFeatures(multMatrix, points)

    if lines:
        lines = projectFeatures(multMatrix, lines)

    if triangles:
        triangles = projectFeatures(multMatrix, triangles)

    return {'points': points, 'lines': lines, 'triangles': triangles}


def projectFeatures(multMatrix, features):
    featureSize = len(features[0])
    featuresMatrix = findTranspose(ungroupListElements(features))
    projectedFeatures = np.dot(multMatrix, featuresMatrix)
    features = groupListElements(findTranspose(projectedFeatures), groupSize=featureSize)
    return features




def allCoordConversions(points, lines, triangles):
    # unit conversion from coordinates to pixels
    # points 
    windowSetObj = windowTracker.windowSetObj

    allPointPixels = []
    for point in points:
        pixelCoords = windowSetObj.coordsToPixel(point[0])
        allPointPixels.append(pixelCoords)

    # lines
    allLinePixels = []
    for line in lines:
        pixelCoords = (windowSetObj.coordsToPixel(line[0]), windowSetObj.coordsToPixel(line[1]))
        allLinePixels.append(pixelCoords)

    # triangles
    allTrianglePixels = []
    for triangle in triangles:
        pixelCoords = (windowSetObj.coordsToPixel(triangle[0]), windowSetObj.coordsToPixel(triangle[1]),
                       windowSetObj.coordsToPixel(triangle[2]))
        allTrianglePixels.append(pixelCoords)

    drawingDict = {'points': allPointPixels, 'lines': allLinePixels, 'triangles': allTrianglePixels}
    return drawingDict











