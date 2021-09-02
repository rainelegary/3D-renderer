from linearAlgebra.schemToDrawing import *

time = __import__("time")  # import time


def main():
    myWindow = createWindow()
    #schematic = combineSchematics([schematicStructure.namedSchematics[schemName].schematic for schemName in schematicStructure.namedSchematics])
    runTime(myWindow) # use varStorage classes to store myWindow globally


def windowLoop(windowSetObj):
    timeStep = rendererMainData.timeStep
    time.sleep(timeStep)

    window = windowSetObj.ownWindow

    schematicStructure.updateSchematics()
    schematic = combineSchematics(addedSchematics=[schematicStructure.namedSchematics[schemName].schematic for schemName in schematicStructure.namedSchematics])


    drawingDictList = updatePoints(windowSetObj, schematic)
    drawFrame(windowSetObj, drawingDictList)
    
    window.update()


def runTime(myWindow):
    while True:
        windowLoop(myWindow)


def createWindow():
    myWindow = WindowSet('the window', '1500x750')
    return myWindow
        

if __name__ == "__main__":
    main()


