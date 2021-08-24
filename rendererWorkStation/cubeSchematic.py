from helperFunctions import *


def cubeSchem(color='#F0F0F0'):

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


    schematicDict = {'points': points, 'lines': lines, 'triangles': triangles, 'color': color}
    return schematicDict


schematics_cubeSchematic = cubeSchem(color='#50E060')
schematics_cubeSchematic['triangles'] = []

schematics_cubeCorners = {'points': cubeSchem()['points'], 'color': 'all'}
schematics_cubeWithoutCorners = combineSchematics(addedSchematics=[cubeSchem(color='#F0F0F0')], subtractedSchematics=[schematics_cubeCorners])
