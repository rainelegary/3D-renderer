from helperFunctions import *
from random import random

def cubeSchem():
    # points
    c0 = -1
    c1 = 1
    points = []
    for xVal in [c0, c1]:
        for yVal in [c0, c1]:
            for zVal in [c0, c1]:
                points.append([xVal, yVal, zVal])

    # lines
    lines = []
    for coordA in points:
        for coordB in points:
            sharedDimCount = 0
            for comp in range(3):
                if coordA[comp] == coordB[comp]:
                    sharedDimCount += 1
            if sharedDimCount == 2:
                lines.append([coordA, coordB])


    # triangles
    triangles = []
    triOriginPoints = []
    for point in points:
        xVal, yVal, zVal = point[0], point[1], point[2]
        if zVal == c0 and xVal == yVal or zVal == c1 and xVal != yVal:
            triOriginPoints.append(point)

    for pointA in triOriginPoints:
        for pointB0 in points:
            for pointB1 in points:
                if pointB0 != pointB1 and countSharedElements(pointA, pointB0) == 2 and countSharedElements(pointA, pointB1) == 2:
                    triangles.append([pointA, pointB0, pointB1])


    schematicDict = {'points': points, 'lines': lines, 'triangles': triangles}
    return schematicDict


def numRatioSchematic(trials):
    points = []
    for trial in range(trials):
        a_kills_b = random()
        a_kills_c = random()
        b_kills_a = random()
        b_kills_c = random()
        c_kills_a = random()
        c_kills_b = random()

        aKDR = (a_kills_b + a_kills_c) / (b_kills_a + c_kills_a)
        bKDR = (b_kills_a + b_kills_c) / (a_kills_b + c_kills_b)
        cKDR = (c_kills_a + c_kills_b) / (a_kills_c + b_kills_c)

        points.append([aKDR, bKDR, cKDR])

    schematicDict = {'points': points, 'lines': [], 'triangles': []}
    return schematicDict



schematics_ratioSchematic = numRatioSchematic(trials=500)

schematics_cubeSchematic = cubeSchem()

schematics_cubeCorners = {'points': cubeSchem()['points']}
schematics_cubeWithoutCorners = combineSchematics(addedSchematics=[cubeSchem()], subtractedSchematics=[schematics_cubeCorners])


