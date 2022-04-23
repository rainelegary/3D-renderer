from listModification import *
from colorLab import *
from schematicFuncs import *


class CubeSchematic(BaseSchematic):
    def __init__(self, cubeRadius, colors, setSpecs):
        self.schematic = []
        self.minCoord = -cubeRadius
        self.maxCoord = cubeRadius
        self.colors = colors
        self.setSpecs = setSpecs

        super().__init__()


    def createSchematic(self):
        theSchemSet = self.createSchemSets()
        self.schematic = [theSchemSet]


    def createSchemSets(self):
        points = self.generatePoints()
        lines = self.generateLines()
        triangles = self.generateTriangles()

        theSchemSet = {}
        theSchemSet['features'] = {'points': points, 'lines': lines, 'triangles': triangles}
        theSchemSet['colors'] = self.colors
        theSchemSet['set specs'] = self.setSpecs
        theSchemSet = fillBlankSet(theSchemSet)

        return theSchemSet


    def generatePoints(self):
        c0 = self.minCoord
        c1 = self.maxCoord
        points = []
        for xVal in [c0, c1]:
            for yVal in [c0, c1]:
                for zVal in [c0, c1]:
                    points.append([[xVal, yVal, zVal]])

        self.points = points
        return points


    def generateLines(self):
        points = self.points

        lines = []
        for coordA in points:
            for coordB in points:
                sharedDimCount = 0
                for comp in range(3):
                    if coordA[0][comp] == coordB[0][comp]:
                        sharedDimCount += 1
                if sharedDimCount == 2:
                    lines.append([coordA[0], coordB[0]])
        
        self.lines = lines
        return lines


    def generateTriangles(self):
        points = self.points
        c0 = self.minCoord
        c1 = self.maxCoord

        triangles = []
        triOriginPoints = []
        for point in points:
            xVal, yVal, zVal = point[0][0], point[0][1], point[0][2]
            if zVal == c0 and xVal == yVal or zVal == c1 and xVal != yVal:
                triOriginPoints.append(point)

        for pointA in triOriginPoints:
            for pointB0 in points:
                for pointB1 in points:
                    if pointB0 != pointB1 and countSharedElements(pointA[0], pointB0[0]) == 2 and countSharedElements(pointA[0], pointB1[0]) == 2:
                        triangles.append([pointA[0], pointB0[0], pointB1[0]])

        self.triangles = triangles
        return triangles

