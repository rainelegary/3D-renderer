
# nuances of dynamic schematics

# keep track of time
# keep track of what the current schematic frame is
# keep track of how many frames the schematic goes through [per second] or [per single increment]

from linearAlgebra.listModification import ungroupListElements
from varStorage import *

class Schematic:
	def __init__(self):
		print("Please override __init__() method for the Schematic class")

	def __iter__(self):
		return iter(self.schematic)

	def removeElements(self, featureTypes):
		schematic = self.schematic
		for featureType in featureTypes:
			for schemSetN in range(len(schematic)):
				schematic[schemSetN][featureType] = []
	
	def updateSchematic(self):
		print("Please override updateSchematic() method for the Schematic class")

	# may want to create a class method that updates all schematics simultaneously
	@classmethod
	def updateAllSchematics(cls):
		print("the class method UpdateAllSchematics() in the Schematic class is not yet implemented")


def createRunningLine(points, closeShape=False):
	if closeShape:
		points.append(points[0])
	
	lines = []
	for pointN in range(len(points)):
		point = points[pointN]
		if pointN > 0:
			lines.append([points[pointN], points[pointN-1]])

	return lines


def combineSchematics(addedSchematics=(), subtractedSchematics=()):
	for negSchem in subtractedSchematics:
		for posSchemN in range(len(addedSchematics)):
			posSchem = addedSchematics[posSchemN]
			
			addedSchematics[posSchemN] = combineSchemSets(addedSchemSets=posSchem, subtractedSchemSets=negSchem)
	
	finalSchematic = ungroupListElements(addedSchematics)
	return finalSchematic

def combineSchemSets(addedSchemSets=(), subtractedSchemSets=()):

    for negSchem in subtractedSchemSets:
        for posSchemN in range(len(addedSchemSets)):
            posSchem = addedSchemSets[posSchemN]
            if negSchem['color'] in ['all', posSchem['color']]:
                posSchem = subtractSchemSet(posSchem, negSchem)
                addedSchemSets[posSchemN] = posSchem
    
    return addedSchemSets


def subtractSchemSet(posSchemSet, negSchemSet):
    for itemType in negSchemSet:
        for item in negSchemSet[itemType]:
            if item in posSchemSet[itemType]:
                posSchemSet[itemType].remove(item)


def updateRotation(ratesOfChange):
	timePassed = time.time() - renderVars.timeCreated
	thetas = [rateOfChange*timePassed for rateOfChange in ratesOfChange]
	return thetas
