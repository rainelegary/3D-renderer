from random import random
from varStorage import *
from schematicFuncs import *


class RatioSchem(BaseSchematic):
    def __init__(self, trials, colors, setSpecs):
        self.trials = trials
        self.colors = colors
        self.setSpecs = setSpecs

        super().__init__()


    def createSchematic(self):
        points = self.runTrials()
        self.schemSet = fillBlankSet({'features': {'points': points}, 'colors': self.colors, 'set specs': self.setSpecs})
        self.schematic = [self.schemSet]
        # self.removeElements('lines', 'triangles')


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

            points.append([[aKDR, bKDR, cKDR]])
        
        return points