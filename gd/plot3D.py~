import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def f(x, y):
    return np.sin(np.sqrt(3*x**2)) - 3 * np.cos(y)+2 * 1/2 *np.cos(y**2)-3 * 5*np.cos(y)

#x = np.arange(-5,5,0.01)
#y = np.arange(-5,5,0.01)
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)



X,Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()

ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
