
from objects import Vector, H,P, Experiment
import numpy as np
import matplotlib.pyplot as plt
import re

FRONT = Vector(0,1)
RIGHT = Vector(1,0)
LEFT = Vector(-1,0)

DIRECTIONS = {'F':FRONT,'R':RIGHT,'L':LEFT, 'S':Vector(0,0)}

R_90 = np.array([[0,1],[-1,0]]) 
L_90 = np.array([[0,-1],[1,0]]) 

def rotate_vector(vec,R):
    if np.all(vec.pos == RIGHT.pos):
        R = np.dot(R,R_90)
    if np.all(vec.pos == LEFT.pos):
        R = np.dot(R,L_90)
    return R

def make_experiment(cells,directions):
    cells = cells.upper()
    cells = re.sub(r'[^HP]+','',cells)
    directions = directions.upper()
    directions = re.sub(r'[^FRLS]+','',directions)
    
    experiment = Experiment()

    for i,cell in enumerate(cells):
        C = H() if cell == 'H' else P()
        d = np.dot(experiment.basis, DIRECTIONS[directions[i]].pos)
        D = Vector(d[0],d[1])
        experiment.add_Cell(C,D)
        experiment.basis = rotate_vector(DIRECTIONS[directions[i]],experiment.basis)

    return experiment
    


exp = make_experiment('HPHPPPP','SFRFRFF')
exp.plot_Experiment()
plt.show()