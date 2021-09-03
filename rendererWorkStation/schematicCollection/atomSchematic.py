import math
import numpy as np
import random
from schematicFuncs import *
from linearAlgebra.specialMatrices import *
from varStorage import *


class AtomSchematic(Schematic):
	def __init__(self, nOrbitals, nElectrons, nOrbitalSteps, electronSize=5):
		self.nOrbitals = nOrbitals
		self.nElectrons = nElectrons
		self.nOrbitalSteps = nOrbitalSteps
		self.electronSize = electronSize

		super().__init__()
	

	def createSchematic(self):
		self.initializeOrbitals()
		self.createSchemSets()


	def updateSchematic(self):
		self.updateElectrons()
		# want to add: 
		# oscillating orbital sizes
		# changing colors, not sure in what way yet
		self.createSchemSets()

	
	def createSchemSets(self):
		schematic = []
		orbitals = self.orbitalSet
		for orbital in orbitals:
			schemSet = {}
			color, points, electrons, pointSize = orbital['color'], orbital['points'], orbital['electron locations'], orbital['point size']
			lines = createRunningLine(points, closeShape=True)


			renderedPoints = [points[elec] for elec in electrons]
			schemSet['color'], schemSet['points'], schemSet['lines'], schemSet['point size'] = color, renderedPoints, lines, pointSize
			schemSet['triangles'] = []
			schematic.append(schemSet)

		self.schematic = schematic


	def initializeOrbitals(self):
		nOrbitals = self.nOrbitals
		nElectrons = self.nElectrons
		nOrbitalSteps = self.nOrbitalSteps
		electronSize = self.electronSize


		phi = (math.sqrt(5)+1)/2
		ellipticalRange = [1, phi*phi]
		radiusRange = [1/phi, phi]
		speedRange = [1/phi, phi]

		allOrbitals = []

		for orbital in range(nOrbitals):
			
			orbitProperties = {'points': [], 'electron locations': [], 'color': '#036BFC', 'point size': electronSize}

			# angles and dynamic radius
			angleRadList = self.dynamicRadius(radiusRange, ellipticalRange, speedRange, nOrbitalSteps)
			orbitProperties['angle & radius list'] = angleRadList
			orbitProperties['rotation speeds'] = [random.uniform(-0.2, 0.2) for i in range(3)]

			# transformation into 3D space
			orbitProperties = self.transformOrbital(orbitProperties)

			allOrbitals.append(orbitProperties)
		
		orbitalSet = self.distributeElectrons(allOrbitals, nElectrons)

		self.orbitalSet = orbitalSet


	def dynamicRadius(self, radiusRange, ellipticalRange, speedRange, nOrbitalSteps):
		axisA = random.uniform(radiusRange[0], radiusRange[1])
		axisB = axisA * random.uniform(ellipticalRange[0], ellipticalRange[1])
		orbitalSpeed = random.uniform(speedRange[0], speedRange[1])
		nSteps = round(nOrbitalSteps/orbitalSpeed)
		angleOffset = random.uniform(0, 2*math.pi)
		angleList = [(stepN*2*math.pi)/nSteps for stepN in range(nSteps)]
		radiusList = [self.calcRadius(axisA, axisB, angleList[i] + angleOffset) for i in range(nSteps)]

		angleRadList = [{'angle': angleList[i], 'radius': radiusList[i]} for i in range(nSteps)]

		return angleRadList


	def calcRadius(self, a, b, t):
		return a*b/math.sqrt(pow(a*math.sin(t), 2)+pow(b*math.cos(t), 2))


	def transformOrbital(self, orbitProperties):
		angleRadList = orbitProperties['angle & radius list']
		nSteps = len(angleRadList)

		thetas = [random.uniform(0, 2*math.pi) for i in range(3)]
		multMatrix = matricesData.regRotationMat(thetas)
		
		cartesianList = self.polarToCartesian(angleRadList)
		pointsMatrix = findTranspose(cartesianList)
		projectedPoints = np.dot(multMatrix, pointsMatrix)
		points = findTranspose(projectedPoints)
		
		orbitProperties['points'] = points

		return orbitProperties


	def polarToCartesian(self, angleRadList):
		cartesianList = []
		for polarCoord in angleRadList:
			angle = polarCoord['angle']
			radius = polarCoord['radius']
			x = math.cos(angle)*radius
			y = math.sin(angle)*radius
			z = 0.0
			cartesianList.append([x, y, z])
		
		return cartesianList


	def distributeElectrons(self, orbitalSet, nElectrons):
		nOrbitals = len(orbitalSet)

		for electronN in range(nElectrons):
			orbitIndex = random.randint(0, nOrbitals - 1)
			nSteps = len(orbitalSet[orbitIndex]['points'])
			startingAngle = random.randint(0, nSteps - 1)

			orbitalSet[orbitIndex]['electron locations'].append(startingAngle)
		
		return orbitalSet


	def updateElectrons(self):
		for orbitalN in range(len(self.orbitalSet)):
			orbital = self.orbitalSet[orbitalN]
			orbital['points'].pop()


			nSteps = len(orbital['points'])
			electrons = orbital['electron locations']
			electrons = self.passElectrons(electrons, nSteps)
			self.orbitalSet[orbitalN]['electron locations'] = electrons


	def passElectrons(self, electrons, nSteps):
		for e in range(len(electrons)):
			if electrons[e] in [nSteps - 1, nSteps]:
				electrons[e] = 0
			else:
				electrons[e] += 1
		return electrons

