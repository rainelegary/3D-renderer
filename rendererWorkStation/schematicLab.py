from helperFunctions import *

from rendererWorkStation.ratioSchematic import *
from rendererWorkStation.cubeSchematic import *
from rendererWorkStation.atomSchematic import *


coolAtom = AtomSchematic(10, 30, 100, bruhIdekConst=1)


schematics_cubeSet = cubeSchem(color='#50E060')
schematics_cubeSet['triangles'] = []
schematics_cubeCornersSet = {'points': cubeSchem()['points'], 'color': 'all'}
schematics_cubeWithoutCornersSet = combineSchematics(addedSchematics=[cubeSchem(color='#F0F0F0')], subtractedSchematics=[schematics_cubeCornersSet])

schematics_ratioSet = numRatioSchematic(trials=500, color='#F0F000')
