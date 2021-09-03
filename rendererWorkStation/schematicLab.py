from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *


def schematicLabMain():
	#customize time step
	global rendererMainData
	rendererMainData = GeneralData()
	rendererMainData.timeStep = 0.01
	rendererMainData.angleRotationRates = [0.120409324, 0.05345673, 0.03738627]


	global schematicStructure
	schematicStructure = schematicLabData()

	#schematics_ratioSet = numRatioSchematic(trials=500, color='#F0F000')
	


class schematicLabData(DataHolder):
	def __init__(self):
		super().__init__()
		self.namedSchematics = {}
		
		self.activateSchematics()


	# Which schematics are being used? 

	def activateSchematics(self):
		self.useAtomSchematic()
		self.useCubeSchematic()
		# self.useRatioSchematic()


	# Customize Schematics

	def useAtomSchematic(self):
		self.coolAtom = AtomSchematic(nOrbitals=5, nElectrons=30, nOrbitalSteps=100, electronSize=5)

		self.addToNamedSchems(self.coolAtom, 'cool atom')


	def useCubeSchematic(self):
		self.coolCube = CubeSchematic(cubeRadius=0.05, color='#50E060', pointSize=2)
		self.coolCube.removeElements('points', 'triangles')

		self.addToNamedSchems(self.coolCube, 'cool cube')


	def useRatioSchematic(self):
		self.coolRatio = RatioSchem(trials=999)

		self.addToNamedSchems(self.coolRatio, 'cool ratio')


	# Customization ends here

	def updateSchematics(self):
		for schemName in self.namedSchematics:
			if self.namedSchematics[schemName]['is dynamic']:
				self.namedSchematics[schemName]['schem object'].updateSchematic()


	def addToNamedSchems(self, schemObject, schemName):
		self.namedSchematics[schemName] = {}
		self.namedSchematics[schemName]['schem object'] = schemObject
		self.namedSchematics[schemName]['is dynamic'] = hasParent(schemObject, 'DynamicSchematic')



schematicLabMain()
