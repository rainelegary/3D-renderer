from mathApplication import *
time = __import__("time")  # import time

main_timeStep = 0.01
main_functionalSchematic = schematics_ratioSchematic
print('this is a test! I repeat, this is a test!')

def main(timeStep, schematic):
    myWindow = WindowSet('the window', '1500x750')
    runTime(timeStep, myWindow, schematic)


def runTime(timeStep, myWindow, schematic):
    mainStartTime = time.time()

    while True:
        time.sleep(timeStep)
        timePassed = time.time() - mainStartTime

        windowLoop(myWindow, timePassed, schematic)

def windowLoop(windowSetObj, timePassed, schematic):
    window = windowSetObj.ownWindow
    canvas = windowSetObj.ownCanvas

    drawingDict = updatePoints(windowSetObj, timePassed, schematic)
    points = drawingDict['points']
    lines = drawingDict['lines']
    triangles = drawingDict['triangles']

    drawFrame(windowSetObj, points=points, lines=lines, triangles=triangles, pointSize=1)

    window.update()


if __name__ == "__main__":
    main(main_timeStep, main_functionalSchematic)


