from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *


def schematicLabScript():
	#customize time step
	global rendererMainData
	rendererMainData = GeneralData()
	rendererMainData.timeStep = 0.01
	rendererMainData.background = '#141030'
	rendererMainData.angleRotationRates = [0.120409324, 0.05345673, 0.03738627] # arbitrary numbers


	global schematicStructure
	schematicStructure = schematicLabData()


	global windowTracker
	windowTracker = WindowData()
	windowTracker.name = 'the window'
	windowTracker.geometry = '1000x500'
	windowTracker.zoom = 100


class schematicLabData(DataHolder):
	def __init__(self):
		super().__init__()
		self.namedSchematics = {}
		
		self.activateSchematics()


	# Which schematics are being used? 

	def activateSchematics(self):
		self.useAtomSchematic()
		self.useCubeSchematic()
		#self.useRatioSchematic()


	# Customize Schematics

	def useAtomSchematic(self):
		self.coolAtom = AtomSchematic(nOrbitals=10, nElectrons=100, nOrbitalSteps=100, electronSize=3)

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

		self.schematic = combineSchematics(addedSchematics=[schematicStructure.namedSchematics[schemName]['schem object'].schematic for schemName in schematicStructure.namedSchematics])


	def addToNamedSchems(self, schemObject, schemName):
		self.namedSchematics[schemName] = {}
		self.namedSchematics[schemName]['schem object'] = schemObject
		self.namedSchematics[schemName]['is dynamic'] = hasParent(schemObject, 'DynamicSchematic')




schematicLabScript()
