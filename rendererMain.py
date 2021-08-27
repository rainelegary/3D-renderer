from schemToDrawing import *
time = __import__("time")  # import time

main_timeStep = 0.01
# main_functionalSchematic = [schematics_ratioSet, schematics_cubeSet]
main_functionalSchematic = coolAtom

def main(timeStep, schematic):
    myWindow = WindowSet('the window', '1500x750')
    runTime(timeStep, myWindow, schematic)


def refreshSchematic(schematic):
    coolAtom.updateSchematic()
    schematic = coolAtom.schematic

    return schematic


def windowLoop(windowSetObj, timePassed, schematic):

    schematic = refreshSchematic(schematic)

    window = windowSetObj.ownWindow
    drawingDictList = updatePoints(windowSetObj, timePassed, schematic)
    drawFrame(windowSetObj, drawingDictList)
    window.update()


def runTime(timeStep, myWindow, schematic):
    mainStartTime = time.time()

    while True:
        time.sleep(timeStep)
        timePassed = time.time() - mainStartTime
        
        windowLoop(myWindow, timePassed, schematic)
        



if __name__ == "__main__":
    main(main_timeStep, main_functionalSchematic)


