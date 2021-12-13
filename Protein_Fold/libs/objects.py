import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = np.array([x,y],dtype=float)

    def rewirtePos(self):
        self.x = self.pos[0]
        self.y = self.pos[1]
    
    def move(self,direction):
        self.pos += direction.pos
        self.rewirtePos()
    
    def copy(self):
        return Vector(self.x,self.y)

class Cell:
    def __init__(self,type,color):
        self.type = type
        self.color = color
    
    def set_position(self,pos):
        self.pos = pos.copy()
        self.center = self.pos.pos+np.array([0.5,0.5])
    
    def plot_cell(self,ax):
        ax.scatter(self.center[0],self.center[1])
        ax.add_patch(Rectangle((self.pos.x+0.12, self.pos.y+0.12), 0.75, 0.75,color=self.color,zorder=3))
        ax.annotate(self.type,(self.center[0],self.center[1]),fontsize=40,va='center',ha='center')

class H(Cell):
    def __init__(self):
        super().__init__('H','#5DD849')

class P(Cell):
    def __init__(self):
        super().__init__('P','#CB5A29')
    
class Experiment:
    def __init__(self,name='Experiment'):
        self.name = name
        self.start_Pos = Vector(0,0)
        self.current_Pos = Vector(0,0)
        self.cells = []
        self.max = [0,1]
        self.min = [0,0]
        self.basis = np.identity(2,dtype=float)

    def add_Cell(self,cell,direction=Vector(1,0)):
        self.current_Pos.move(direction)
        cell.set_position(self.current_Pos.copy())
        self.cells.append(cell)

        max_x = self.max[0] if self.max[0] > self.current_Pos.x else self.current_Pos.x
        max_y = self.max[1] if self.max[1] > self.current_Pos.y else self.current_Pos.y
        min_x = self.min[0] if self.min[0] < self.current_Pos.x else self.current_Pos.x
        min_y = self.min[1] if self.min[1] < self.current_Pos.y else self.current_Pos.y

        self.max = [max_x,max_y]
        self.min = [min_x,min_y]

    def plot_Experiment(self):
        fig,ax = plt.subplots(figsize=(10,10))
        ax.set_xlim(self.min[0],self.max[0]+1)
        ax.set_ylim(self.min[1],self.max[1]+1)
        ax.set_aspect('equal')
        line = []
        for cell in self.cells:
            line.append(cell.center)
        line = np.array(line)
        ax.plot(line[:,0],line[:,1],color='black',lw=5)
        for cell in self.cells:
            cell.plot_cell(ax)
