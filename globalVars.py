import time
import math

class DataHolder:
	def __init__(self):
		self.info = {}
		self.timeCreated = time.time()
		self.angleRotationRates = [1/math.e, math.pi/3, 1]



global renderVars
renderVars = DataHolder()
