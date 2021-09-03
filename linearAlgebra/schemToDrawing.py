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



def doProjections(multMatrix, points, lines, triangles): # to be separated into smaller bits

    # point projection
    if points:
        pointsMatrix = findTranspose(points)
        projectedPoints = np.dot(multMatrix, pointsMatrix)
        points = findTranspose(projectedPoints)

    # line projection
    if lines:
        linePoints = ungroupListElements(lines)
        linesMatrix = findTranspose(linePoints)
        projectedLines = np.dot(multMatrix, linesMatrix)
        lines = groupListElements(findTranspose(projectedLines), groupSize=2)

    # triangle projection
    if triangles:
        trianglePoints = ungroupListElements(triangles)
        trianglesMatrix = findTranspose(trianglePoints)
        projectedTriangles = np.dot(multMatrix, trianglesMatrix)
        triangles = groupListElements(findTranspose(projectedTriangles), groupSize=3)

    return {'points': points, 'lines': lines, 'triangles': triangles}


def allCoordConversions(points, lines, triangles):
    # unit conversion from coordinates to pixels
    # points 
    windowSetObj = windowTracker.windowSetObj

    allPointPixels = []
    for point in points:
        pixelCoords = windowSetObj.coordsToPixel(point)
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











