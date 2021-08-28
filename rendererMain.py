from linearAlgebra.schemToDrawing import *

time = __import__("time")  # import time


def main():
    myWindow = WindowSet('the window', '1500x750')
    schematic = usedSchematics.currentSchematic
    runTime(myWindow) # use varStorage classes to store myWindow globally


def windowLoop(windowSetObj):
    timeStep = rendererMainData.timeStep
    time.sleep(timeStep)

    window = windowSetObj.ownWindow

    usedSchematics.updateSchematics()
    schematic = usedSchematics.currentSchematic

    drawingDictList = updatePoints(windowSetObj, schematic)
    drawFrame(windowSetObj, drawingDictList)
    window.update()


def runTime(myWindow):
    while True:
        windowLoop(myWindow)
        



if __name__ == "__main__":
    main()


