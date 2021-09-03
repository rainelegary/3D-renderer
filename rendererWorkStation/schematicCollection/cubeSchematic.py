from listModification import *
from varStorage import *
from schematicFuncs import *


class CubeSchematic(BaseSchematic):
    def __init__(self, cubeRadius, color='#F0F0F0', pointSize=2):
        self.schematic = []
        self.minCoord = -cubeRadius
        self.maxCoord = cubeRadius
        self.color = color
        self.pointSize = pointSize

        super().__init__()


    def createSchematic(self):
        theSchemSet = self.createSchemSets()
        self.schematic = [theSchemSet]


    def createSchemSets(self):
        points = self.generatePoints()
        lines = self.generateLines()
        triangles = self.generateTriangles()

        theSchemSet = {}
        theSchemSet['points'], theSchemSet['lines'], theSchemSet['triangles'] = points, lines, triangles
        theSchemSet['color'] = self.color
        theSchemSet['point size'] = self.pointSize

        return theSchemSet


    def generatePoints(self):
        c0 = self.minCoord
        c1 = self.maxCoord
        points = []
        for xVal in [c0, c1]:
            for yVal in [c0, c1]:
                for zVal in [c0, c1]:
                    points.append([xVal, yVal, zVal])

        self.points = points
        return points


    def generateLines(self):
        points = self.points

        lines = []
        for coordA in points:
            for coordB in points:
                sharedDimCount = 0
                for comp in range(3):
                    if coordA[comp] == coordB[comp]:
                        sharedDimCount += 1
                if sharedDimCount == 2:
                    lines.append([coordA, coordB])
        
        self.lines = lines
        return lines


    def generateTriangles(self):
        points = self.points
        c0 = self.minCoord
        c1 = self.maxCoord

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

        self.triangles = triangles
        return triangles

