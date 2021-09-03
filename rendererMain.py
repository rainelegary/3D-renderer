from linearAlgebra.schemToDrawing import *
import time


def main():
    createWindow()
    runTime()


def createWindow():
    myWindow = WindowSet(windowTracker.name, windowTracker.size)
    windowTracker.windowSetObj = myWindow


def runTime():
    while True:
        time.sleep(rendererMainData.timeStep)
        windowLoop()


def windowLoop():
    schematicStructure.updateSchematics()
    redrawCanvas(schemToStrokes(schematicStructure.schematic))
    windowTracker.windowSetObj.ownWindow.update()


if __name__ == "__main__":
    main()


