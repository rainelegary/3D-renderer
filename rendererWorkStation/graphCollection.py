import math

class CustomGraph():
	def __init__(self):
		pass

	def mainFunction(self):
		print("mainFunction must be overridden by each child class of CustomGraph")

class Sinusoidal(CustomGraph):
	def __init__(self, amplitude, wavelength, angleOffset):
		self.amplitude = amplitude
		self.wavelength = wavelength
		self.angleOffset = angleOffset
	
	def mainFunction(self, x):
		return self.amplitude*math.sin((x - self.angleOffset)/self.wavelength)






