import math
import numpy as np
import random


def initializeAtom(nOrbitals, nElectrons, nOrbitalSteps, bruhIdekConst=0):
	phi = (math.sqrt(5)+1)/2
	ellipticalRange = [1, phi*phi]
	radiusRange = [1/phi, phi]
	speedRange = [1/phi, phi]

	orbitalSet = []

	for orbital in range(nOrbitals):
		
		orbitProperties = {'points': [], 'electron starts': [], 'idk constant': bruhIdekConst}

		# angles and dynamic radius
		angleRadList = dynamicRadius(radiusRange, ellipticalRange, speedRange, nOrbitalSteps)
		orbitProperties[orbital]['angle & radius list'] = angleRadList

		# transformation into 3D space
		orbitProperties = transformOrbital(orbitProperties)

		orbitalSet.append(orbitProperties)
	
	orbitalSet = distributeElectrons(orbitalSet, nElectrons)


def distributeElectrons(orbitalSet, nElectrons):
	nOrbitals = len(orbitalSet)

	for electronN in range(nElectrons):
		orbitIndex = random.randint(0, nOrbitals - 1)
		nSteps = len(orbitalSet[orbitIndex]['points'])
		startingAngle = random.randint(0, nSteps - 1)

		orbitalSet[orbitIndex]['electron starts'].append(startingAngle)
	
	return orbitalSet


def dynamicRadius(radiusRange, ellipticalRange, speedRange, nOrbitalSteps):
	axisA = random.uniform(radiusRange[0], radiusRange[1])
	axisB = axisA * random.uniform(ellipticalRange[0], ellipticalRange[1])
	orbitalSpeed = random.uniform(speedRange[0], speedRange[1])
	nSteps = nOrbitalSteps/orbitalSpeed
	angleOffset = random.uniform(0, 2*math.pi)
	angleList = [(stepN*2*math.pi)/nSteps for stepN in range(nSteps)]
	radiusList = [calcRadius(axisA, axisB, angleList[i] + angleOffset) for i in range(nSteps)]

	angleRadList = [{'angle': angleList[i], 'radius': radiusList[i]} for i in range(nSteps)]

	return angleRadList


def transformOrbital(orbitProperties):
	bruhIdekConst = orbitProperties['idk constant']
	angleRadList = orbitProperties['angle & radius list']
	nSteps = len(angleRadList)

	normalVector = randomVector(3)
	seedVector = randomVector(3)
	baseVector = convertToUnitVec(np.cross(normalVector, seedVector))
	
	idkMatrix = np.array([baseVector, normalVector, seedVector])
	multMatrix = np.linalg.inv(idkMatrix)

	angleList = [el['angle'] for el in angleRadList]
	radiusList = [el['radius'] for el in angleRadList]

	for stepN in range(nSteps):
		angle, radius = angleList[stepN], radiusList[stepN]
		angleVector = [math.cos(angle), 0, bruhIdekConst]
		pointVec = [component for component in np.dot(multMatrix, angleVector)]
		distance = math.sqrt(sum(el*el for el in pointVec))
		point = [el*radius/distance for el in pointVec]

		orbitProperties['points'].append(point)

	return orbitProperties

		
def randomVector(dimensions):
    components = [np.random.normal() for i in range(dimensions)]
    length = math.sqrt(sum(x*x for x in components))
    vector = [x/length for x in components]
    return vector


def convertToUnitVec(vector):
	length = math.sqrt(sum(x*x for x in vector))
	for i in range(len(vector)):
		vector[i] /= length
	
	return vector


def calcRadius(a, b, t):
	return a*b/math.sqrt(pow(a*math.sin(t), 2)+pow(b*math.cos(t), 2))



initializeAtom(1, 1, 100)