from varStorage import *

def colorLabScript():
	global colorPalettes
	colorPalettes = ColorData()


class ColorData(DataHolder):
	def __init__(self):
		super().__init__()
		self.colorLists()
		self.namedColors()
		self.schematicThemes()


	def schematicThemes(self):
		pass


	def namedColors(self):
		self.backgrounds = {'blue void': '#141030', 'endless void': '#050b1a', 'light sky': '#a8ace0', 'bright sky': '#a8ace0'}
		self.drawing = {'chalk': '#F0F0F0', }


	def colorLists(self):
		self.fire = ['#FFCD06', '#F6960E', '#EE771C', '#E45323', '#D23008']
		self.ocean = ['#ABD7EC', '#59C1E8', '#3585DA', '#1061B0', '#003C72']
		self.electric = ['#FDE9AA', '#FFE981', '#fff98a', '#3c69c3', '#1f3665']
	


colorLabScript()