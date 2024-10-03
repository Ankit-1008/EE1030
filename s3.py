#Code by GVV Sharma
#July 22, 2024
#released under GNU GPL
#Line 


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/ankit/matgeo/codes/CoordGeo/')
import numpy as np
import mpmath as mp
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen





#Given points
A = np.array(([5, 2])).reshape(-1,1) 
B = np.array(([2, 3])).reshape(-1,1) 
C = np.array(([41/17, 23/17])).reshape(-1,1) 
D = np.array(([2, 3])).reshape(-1,1) 

k1 = -3
k2 = 3


#Generating Lines
x_AC = line_gen(A,C)
x_AB = line_gen(C,B)
#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$distance(AC)$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$distance(AB)$')
colors = np.arange(1,4)
#Labeling the coordinates
tri_coords = np.block([A,B,C])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A(5,2)','B(2,3)','C(41/17,23/17)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
    #plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-10,-5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# use set_position
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
'''
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
'''
plt.grid() # minor
plt.axis('equal')

plt.show()
