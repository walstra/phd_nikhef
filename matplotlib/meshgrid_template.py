from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

step = 0.04
maxval = 1.0
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

###########
#create points in polar coordinates
###create 50 float values between 0 and 1.25 using numpy
r =
 
##########
##create 50 float values between 0 and 2 pi
p = 

R,P = np.meshgrid(r,p) #look up the details on internet!

#transform your r and p vectors to a cartesian system
x,y = 
z = ((R**2-1)**2)
ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap=cm.YlGnBu_r)
ax.set_zlim3d(0,1)
ax.set_xlabel(r'$\phi_\mathrm{rea})$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$\phi$')
plt.show()
