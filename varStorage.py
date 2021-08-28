import time
import math


def globalVarsScript():
	global renderVars
	renderVars = DataHolder()


class DataHolder:
	def __init__(self):
		self.info = {}
		self.timeCreated = time.time()


class GeneralData(DataHolder):
	def __init__(self):
		self.timeCreated = time.time()





globalVarsScript()
