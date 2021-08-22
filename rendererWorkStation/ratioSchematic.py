from random import random

def numRatioSchematic(trials, color='#F0F0F0'):
    points = []
    for trial in range(trials):
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

    schematicDict = {'points': points, 'lines': [], 'triangles': [], 'color': color}
    return schematicDict



schematics_ratioSchematic = numRatioSchematic(trials=500, color='#F0F000')