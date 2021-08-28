from varStorage import *

from linearAlgebra.matrixOperations import *


class UniqueMatrices(DataHolder):
	def __init__(self):
		pass

	def rotationProjMat(self, thetas):
		thetaX, thetaY, thetaZ = [theta for theta in thetas]
		xRotationMatrix, yRotationMatrix, zRotationMatrix = self.rotationInX(thetaX), self.rotationInY(thetaY), self.rotationInZ(thetaZ)
		ortho_matrix = self.orthoMatrix()
		
		finalMatrix = combineMatrices(xRotationMatrix, yRotationMatrix, zRotationMatrix, ortho_matrix)
		return finalMatrix

	def identityMat(self):
		idMat =[
			[1, 0, 0],
			[0, 1, 0],
			[0, 0, 1],
		]
		return idMat


	def orthoMatrix(self):
		ortho_matrix = [
			[1, 0, 0],
			[0, 1, 0],
		]
		return ortho_matrix


	def rotationInX(self, thetaX):
			rotationX = [
				[1, 0, 0],
				[0, math.cos(thetaX), -math.sin(thetaX)],
				[0, math.sin(thetaX), math.cos(thetaX)],
			]
			return rotationX

	def rotationInY(self, thetaY):
		rotationY = [
			[math.cos(thetaY), 0, -math.sin(thetaY)],
			[0, 1, 0],
			[math.sin(thetaY), 0, math.cos(thetaY)],
		]

		return rotationY


	def rotationInZ(self, thetaZ):
		rotationZ = [
			[math.cos(thetaZ), -math.sin(thetaZ), 0],
			[math.sin(thetaZ), math.cos(thetaZ), 0],
			[0, 0, 1],
		]
		return rotationZ


