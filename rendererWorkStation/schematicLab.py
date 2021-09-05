from rendererWorkStation.schematicCollection.ratioSchematic import *
from rendererWorkStation.schematicCollection.cubeSchematic import *
from rendererWorkStation.schematicCollection.atomSchematic import *

from varStorage import *


def schematicLabScript():
	#customize time step
	global rendererMainData
	rendererMainData = GeneralData()
	rendererMainData.timeStep = 0.01
	rendererMainData.background = colorPalettes.backgrounds['blue void']
	rendererMainData.angleRotationRates = [0.120409324, 0.05345673, 0.03738627] # arbitrary numbers


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
		colors = {'orbital colors': colorPalettes.ocean, 'electron fill': '#F0F0F0', 'electron outline': '#F0F0F0'}
		setSpecs = {'electron size': 3, 'line width': 1.5}
		orbitalSettings = {}

		phi = (math.sqrt(5)+1)/2
		orbitalSettings['elliptical range'] = [phi, phi]
		orbitalSettings['radius range'] = [1, 1]
		orbitalSettings['speed range'] = [1/phi, phi]

		schemObject = AtomSchematic(nOrbitals=10, nElectrons=100, nOrbitalSteps=100, colors=colors,
					    setSpecs=setSpecs, orbitalSettings=orbitalSettings)
		includedFeatures = {'points': True, 'lines': True}

		if visible: self.addToNamedSchems(schemName, schemObject, includedFeatures)


	def customizeCube(self):
		visible = True
		schemName = 'cool cube'
		colors = {'line color': colorPalettes.fire[0]}
		setSpecs = {'line width': 1}
		schemObject = CubeSchematic(cubeRadius=0.05, colors=colors, setSpecs=setSpecs)
		includedFeatures = {'points': False, 'lines': True, 'triangles': False}

		if visible: self.addToNamedSchems(schemName, schemObject, includedFeatures)

	
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
		self.customizeRatio()


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
