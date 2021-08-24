tk = __import__("tkinter")  # import tkinter as tk

graphics_pointSize = 0.1

class WindowSet:
    def __init__(self, title, geometry, zoom=50, background='#303030', lineColor='#F0F0F0'):
        self.ownWindow = tk.Tk()
        self.ownCanvas = None
        self.title = title

        self.geometry = geometry
        self.width = int(geometry.split('x')[0])
        self.height = int(geometry.split('x')[1])
        self.zoom = zoom

        self.background = background
        self.lineColor = lineColor

        self.initUI()

    def initUI(self):
        ownWindow = self.ownWindow
        ownWindow.title(self.title)
        ownWindow.geometry(self.geometry)

        ownCanvas = tk.Canvas(ownWindow, bg=self.background)
        ownCanvas.place(x=0, y=0, width=self.width, height=self.height)

        self.ownWindow = ownWindow
        self.ownCanvas = ownCanvas

    def coordsToPixel(self, coordsGiven):
        xIn = coordsGiven[0]
        yIn = coordsGiven[1]

        xOut = xIn * self.zoom + self.width / 2
        yOut = yIn * self.zoom + self.height / 2

        return xOut, yOut


def drawFrame(windowObject, drawingDictList, pointSize=2):
    canvasObject = windowObject.ownCanvas
    canvasObject.delete("all")

    for drawingDict in drawingDictList:

        color = drawingDict['color']

        for point in drawingDict['points']:
            canvasObject.create_oval(point[0]-pointSize/2, point[1]-pointSize/2, point[0]+pointSize/2, point[1]+pointSize/2,
                                    fill=windowObject.lineColor, outline=color)

        for line in drawingDict['lines']:
            canvasObject.create_line(line, fill=color)

        for triangle in drawingDict['triangles']:
            canvasObject.create_polygon(triangle, fill=color)


# def coordsToPixel(coords):
#     xIn = coords[0]
#     yIn = coords[1]

#     xOut = xIn * 50 + 750
#     yOut = yIn * 50 + 375

#     return xOut, yOut

