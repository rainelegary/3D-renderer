from random import random
from varStorage import *
from schematicFuncs import *


class RatioSchem(BaseSchematic):
    def __init__(self, trials, color='#F0F0F0', pointSize=2):
        self.trials = trials
        self.color = color
        self.pointSize = pointSize

        super().__init__()


    def createSchematic(self):
        points = self.runTrials()
        self.schematic = [{'points': points, 'color': self.color, 'point size': self.pointSize}]
        self.removeElements('lines', 'triangles')


    def runTrials(self):
        points = []
        for trial in range(self.trials):
            a_kills_b = random()
            a_kills_c = random()
            b_kills_a = random()
            b_kills_c = random()
            c_kills_a = random()
            c_kills_b = random()

            aKDR = (a_kills_b + a_kills_c) / (b_kills_a + c_kills_a)
            bKDR = (b_kills_a + b_kills_c) / (a_kills_b + c_kills_b)
            cKDR = (c_kills_a + c_kills_b) / (a_kills_c + b_kills_c)

            points.append([aKDR, bKDR, cKDR])
        
        return points