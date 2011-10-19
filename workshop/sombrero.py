from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def sombrero(c=None):
    if c:
        R = np.sqrt((c[0]-2*np.exp(1))**2 + (c[1]-np.pi)**2)
        Z = np.sin(1) - (np.sin(R)/R)
        return Z
    else:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        #ax = Axes3D(fig, azim = -128, elev = 43)
        X = np.arange(0, 10, 0.2)
        Y = np.arange(0, 10, 0.2)
        X, Y = np.meshgrid(X, Y)
        Z = np.reshape(sombrero([X, Y]), X.shape)

        #plot_surface(linewidth=0) or plot_wireframe
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, cmap=cm.jet)
        #ax.set_zlim(-1.01, 1.01)

        #ax.zaxis.set_major_locator(LinearLocator(10))
        #ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        #fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()

def main():
    sombrero()

if __name__ == '__main__':
    status = main()
