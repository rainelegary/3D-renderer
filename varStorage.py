import time


def globalVarsScript():
	global renderVars
	renderVars = DataHolder()


class DataHolder:
	def __init__(self):
		self.info = {}
		self.timeCreated = time.time()


class GeneralData(DataHolder):
	def __init__(self):
		super().__init__()


class WindowData(DataHolder):
	def __init__(self):
		super().__init__()






globalVarsScript()
