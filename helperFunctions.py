import sys

def ungroupListElements(outerList):
    ungrouped = []
    for subList in outerList:
        for item in subList:
            ungrouped.append(item)
    return ungrouped


def groupListElements(givenList, groupSize):
    if len(givenList) % groupSize != 0:
        sys.exit("func groupListElements: list not evenly divisible by group size")

    groupedList = []
    for groupN in range(len(givenList) // groupSize):
        innerList = []
        for itemN in range(groupSize):
            innerList.append(givenList[groupN * groupSize + itemN])

        groupedList.append(innerList)

    return groupedList


def countSharedElements(listA=(), listB=(), orderMatters=True):
    sharedElements = 0
    if orderMatters:
        for index in range(len(listA)):
            if listA[index] == listB[index]:
                sharedElements += 1

    if not orderMatters:
        for item in listA:
            if item in listB:
                sharedElements += 1

    return sharedElements


def combineSchematics(addedSchematics=(), subtractedSchematics=()):

    for negSchem in subtractedSchematics:
        for posSchemN in range(len(addedSchematics)):
            posSchem = addedSchematics[posSchemN]
            if negSchem['color'] in ['all', posSchem['color']]:
                posSchem = subtractSchematic(posSchem, negSchem)
                addedSchematics[posSchemN] = posSchem
    
    return addedSchematics



def subtractSchematic(posSchem, negSchem):
    for itemType in negSchem:
        for item in negSchem[itemType]:
            if item in posSchem[itemType]:
                posSchem[itemType].remove(item)
