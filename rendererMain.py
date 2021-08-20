from mathApplication import *
time = __import__("time")  # import time

main_timeStep = 0.01
main_functionalSchematicList = [schematics_ratioSchematic, schematics_cubeSchematic]

def main(timeStep, schematicList):
    myWindow = WindowSet('the window', '1500x750')
    runTime(timeStep, myWindow, schematicList)


def runTime(timeStep, myWindow, schematicList):
    mainStartTime = time.time()

    while True:
        time.sleep(timeStep)
        timePassed = time.time() - mainStartTime

        windowLoop(myWindow, timePassed, schematicList)
        

def windowLoop(windowSetObj, timePassed, schematicList):
    window = windowSetObj.ownWindow
    canvas = windowSetObj.ownCanvas

    drawingDictList = updatePoints(windowSetObj, timePassed, schematicList)

    drawFrame(windowSetObj, drawingDictList, pointSize=1)

    window.update()


if __name__ == "__main__":
    main(main_timeStep, main_functionalSchematicList)


