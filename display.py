import tkinter as tk
from rendererWorkStation.schematicLab import *


class WindowSet:
    def __init__(self):
        self.ownWindow = tk.Tk()
        self.ownCanvas = None

        self.initDisplay()


    def initDisplay(self):
        ownWindow = self.ownWindow
        self.ownWindow.title(windowTracker.name)
        self.ownWindow.geometry(windowTracker.geometry)

        self.width = int(windowTracker.geometry.split('x')[0])
        self.height = int(windowTracker.geometry.split('x')[1])
        self.zoom = windowTracker.zoom

        self.ownCanvas = tk.Canvas(ownWindow, bg=rendererMainData.background)
        self.ownCanvas.place(x=0, y=0, width=self.width, height=self.height)


    def coordsToPixel(self, coordsGiven):
        xOut = coordsGiven[0] * self.zoom + self.width / 2
        yOut = coordsGiven[1] * self.zoom + self.height / 2
        return xOut, yOut


    def redrawCanvas(self, drawingDictList):
        self.ownCanvas.delete("all")

        for drawingDict in drawingDictList:
            self.drawFeatures(drawingDict)


    def drawFeatures(self, drawingDict):
        points = drawingDict['points']
        lines = drawingDict['lines']
        triangles = drawingDict['triangles']
        color = drawingDict['color']
        pointSize = drawingDict['point size']

        self.drawPoints(points, color, pointSize)
        self.drawLines(lines, color)
        self.drawTriangles(triangles, color)

    
    def drawPoints(self, points, color, pointSize):
         for point in points:
             self.ownCanvas.create_oval(point[0][0]-pointSize/2, point[0][1]-pointSize/2, point[0][0]+pointSize/2, point[0][1]+pointSize/2,
                                    fill=color, outline=color)


    def drawLines(self, lines, color):
         for line in lines:
            self.ownCanvas.create_line(line, fill=color)

    
    def drawTriangles(self, triangles, color):
        for triangle in triangles:
            self.ownCanvas.create_polygon(triangle, fill=color)




