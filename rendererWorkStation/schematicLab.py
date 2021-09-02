from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *


def schematicLabMain():
	#customize time step
	global rendererMainData
	rendererMainData = GeneralData()
	rendererMainData.timeStep = 0.01
	rendererMainData.angleRotationRates = [1/math.e, math.pi/3, 1]


	global schematicStructure
	schematicStructure = schematicLabData()

	#schematics_ratioSet = numRatioSchematic(trials=500, color='#F0F000')
	


class schematicLabData(DataHolder):
	def __init__(self):
		super().__init__()
		self.namedSchematics = {}
		
		self.activateSchematics()


	def activateSchematics(self):
		self.useAtomSchematic()
		self.useCubeSchematic()


	def updateSchematics(self):
		schemNames = self.namedSchematics
		for schemName in self.namedSchematics:
			self.namedSchematics[schemName].updateSchematic()


	def useAtomSchematic(self):
		self.coolAtom = AtomSchematic(nOrbitals=5, nElectrons=10, nOrbitalSteps=100, electronSize=5)
		self.namedSchematics['cool atom'] = self.coolAtom


	def useCubeSchematic(self):
		self.coolCube = CubeSchematic(cubeRadius=1, color='#50E060', pointSize=2)
		self.coolCube.removeElements(['points', 'triangles'])
		self.namedSchematics['cool cube'] = self.coolCube


schematicLabMain()
