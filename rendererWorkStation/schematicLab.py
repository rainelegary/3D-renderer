from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *

# customize time step
global rendererMainData
rendererMainData = GeneralData()
rendererMainData.timeStep = 0.01
rendererMainData.angleRotationRates = [1/math.e, math.pi/3, 1]


class schematicLabData(DataHolder):
	def __init__(self):
		super().__init__()
		self.namedSchematics = {}
		self.currentSchematic = []

		self.useAtomSchematic()


	def updateSchematics(self):

		self.coolAtom.updateSchematic()
		schematic = self.coolAtom.schematic
		self.currentSchematic = schematic

	
	def useAtomSchematic(self):
		self.coolAtom = AtomSchematic(nOrbitals=5, nElectrons=10, nOrbitalSteps=100, electronSize=5)
		self.namedSchematics['cool atom'] = self.coolAtom
		# coolAtomSchem = coolAtom.schematic
	


	def useCubeSchematic(self):
		cube = cubeSchem(color='#50E060')
		cube['triangles'] = []
		cubeCorners = {'points': cubeSchem()['points'], 'color': 'all'}
		cubeWithoutCorners = combineSchematics(addedSchematics=[cubeSchem(color='#F0F0F0')], subtractedSchematics=[cubeCorners])

		self.currentSchematic.append(cubeWithoutCorners)


global usedSchematics
usedSchematics = schematicLabData()

schematics_ratioSet = numRatioSchematic(trials=500, color='#F0F000')
