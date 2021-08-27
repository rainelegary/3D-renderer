from specialMatrices import *
from listModification import *
from rendererWorkStation.schematicLab import *
from display import *


def updatePoints(windowSetObj, timePassed, schematicList):
    drawingDictList = []

    for schematic in schematicList:
        points, lines, triangles = schematic['points'], schematic['lines'], schematic['triangles']

        geometry = doProjections(points, lines, triangles)
        points, lines, triangles = [geometry[i] for i in ['points', 'lines', 'triangles']]

        drawingDict = moveTo2D(windowSetObj, points, lines, triangles)

        drawingDict['color'] = schematic['color']
        drawingDict['point size'] = schematic['point size']

        drawingDictList.append(drawingDict)

    return drawingDictList



def doProjections(points, lines, triangles):
    thetaSpeeds = renderVars.angleRotationRates
    thetas = updateRotation(thetaSpeeds)
    finalMatrix = generateProjMat(thetas)

    # point projection
    if points:
        pointsMatrix = findTranspose(points)
        projectedPoints = finalMatrix.matMul(pointsMatrix)
        points = findTranspose(projectedPoints)

    # line projection
    if lines:
        linePoints = ungroupListElements(lines)
        linesMatrix = findTranspose(linePoints)
        projectedLines = finalMatrix.matMul(linesMatrix)
        lines = groupListElements(findTranspose(projectedLines), groupSize=2)

    # triangle projection
    if triangles:
        trianglePoints = ungroupListElements(triangles)
        trianglesMatrix = findTranspose(trianglePoints)
        projectedTriangles = finalMatrix.matMul(trianglesMatrix)
        triangles = groupListElements(findTranspose(projectedTriangles), groupSize=3)

    return {'points': points, 'lines': lines, 'triangles': triangles}


def moveTo2D(windowSetObj, points, lines, triangles):
    # unit conversion from coordinates to pixels
    # points
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











