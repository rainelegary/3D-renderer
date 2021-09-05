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
        features = drawingDict['features']
        colors = drawingDict['colors']
        pointSize = drawingDict['point size']
        outlineTriangles = drawingDict['outline triangles']
        lineWidth = drawingDict['line width']

        self.drawPoints(features['points'], colors['point fill'], colors['point outline'], pointSize)
        self.drawLines(features['lines'], colors['line color'], lineWidth=lineWidth)
        self.drawTriangleFills(features['triangles'], colors['triangle fill'])
        if outlineTriangles: self.drawTriangleOutlines(features['triangles'], colors['triangle outline'], lineWidth)
    

    def drawPoints(self, points, fillColor, outlineColor, pointSize):
         for point in points:
             self.ownCanvas.create_oval(point[0][0]-pointSize/2, point[0][1]-pointSize/2, point[0][0]+pointSize/2, point[0][1]+pointSize/2,
                                    fill=fillColor, outline=outlineColor)


    def drawLines(self, lines, color, lineWidth):
         for line in lines:
            self.ownCanvas.create_line(line, fill=color, width=lineWidth)

    
    def drawTriangleFills(self, triangles, fillColor):
        for triangle in triangles:
            self.ownCanvas.create_polygon(triangle, fill=fillColor)


    def drawTriangleOutlines(self, triangles, outlineColor, outlineWidth):
        for triangle in triangles:
                outline = createRunningLine(triangle)
                self.drawLines(outline, outlineColor, outlineWidth)




