from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *


def schematicLabScript():
	#customize time step
	global rendererMainData
	rendererMainData = GeneralData()
	rendererMainData.timeStep = 0.01
  
	rendererMainData.background = colorPalettes.backgrounds['endless void']
	rotationMultiplier = 5
	rendererMainData.angleRotationRates = [
		0.120409324*rotationMultiplier, 
		0.05345673*rotationMultiplier, 
		0.03738627*rotationMultiplier
		] # arbitrary numbers


	global schematicStructure
	schematicStructure = schematicLabData()


	global windowTracker
	windowTracker = WindowData()
	windowTracker.name = 'the window'
	windowTracker.geometry = '1000x500'
	windowTracker.zoom = 100


class schematicLabData(DataHolder):


	# Customize schematics	

	def customizeAtom(self):
		visible = True
		schemName = 'cool atom'
		schemObject = AtomSchematic(nOrbitals=6, nElectrons=100, nOrbitalSteps=100, electronSize=2.5)
		includedFeatures = {'points': True, 'lines': True}

		if visible: 
			self.addToNamedSchems(schemName, schemObject, includedFeatures)


	def customizeCube(self):
		visible = True
		schemName = 'cool cube'
		schemObject = CubeSchematic(cubeRadius=0.05, color=colorPalettes.electric[2], pointSize=2)
		includedFeatures = {'points': False, 'lines': True, 'triangles': False}

		if visible: 
			self.addToNamedSchems(schemName, schemObject, includedFeatures)

	
	def customizeRatio(self):
		visible = False
		schemName = 'cool ratio'
		colors = {'point fill': '#00F000', 'point outline': '#00F000'}
		setSpecs = {}
		schemObject = RatioSchem(trials=999, colors=colors, setSpecs=setSpecs)
		includedFeatures = {'points': True}

		if visible: self.addToNamedSchems(schemName, schemObject, includedFeatures)

	# Customization ends here


	def __init__(self):
		super().__init__()
		self.namedSchematics = {}

		self.activateSchematics()


	def activateSchematics(self):
		self.customizeAtom()
		self.customizeCube()
		# self.customizeRatio()


	def updateSchematics(self):
		for schemName in self.namedSchematics:
			if self.namedSchematics[schemName]['is dynamic']:
				self.namedSchematics[schemName]['schem object'].updateSchematic()

		self.removeDiscludedFeatures()
		self.schematic = combineSchematics(addedSchematics=[schematicStructure.namedSchematics[schemName]['schem object'].schematic for schemName in schematicStructure.namedSchematics])


	def addToNamedSchems(self, schemName, schemObject, includedFeatures):
		self.namedSchematics[schemName] = {}
		self.namedSchematics[schemName]['schem object'] = schemObject
		self.namedSchematics[schemName]['is dynamic'] = hasParent(schemObject, 'DynamicSchematic')
		self.namedSchematics[schemName]['included features'] = includedFeatures
		self.namedSchematics[schemName]['presets'] = {}


	def removeDiscludedFeatures(self):
		for schemName in self.namedSchematics:
			for featureType in self.namedSchematics[schemName]['included features']:
				if not self.namedSchematics[schemName]['included features'][featureType]:
					self.namedSchematics[schemName]['schem object'].removeElements(featureType)


schematicLabScript()
