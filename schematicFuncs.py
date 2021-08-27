# nuances of dynamic schematics

# keep track of time
# keep track of what the current schematic frame is
# keep track of how many frames the schematic goes through [per second] or [per single increment]

class Schematic:
	def __init__(self):
		print("Please override __init__() method for the Schematic class")
	
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
            if negSchem['color'] in ['all', posSchem['color']]:
                posSchem = subtractSchematic(posSchem, negSchem)
                addedSchematics[posSchemN] = posSchem
    
    return addedSchematics



def subtractSchematic(posSchem, negSchem):
    for itemType in negSchem:
        for item in negSchem[itemType]:
            if item in posSchem[itemType]:
                posSchem[itemType].remove(item)