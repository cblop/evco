from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def sombrero(c=None):
    if c:
        R = (c[0]-2*np.exp(1))**2 + (c[1]-np.pi)**2 + 1
        Z = np.sin(1) - (np.sin(R)/R)
        return Z
    else:
        fig = plt.figure()
        ax = Axes3D(fig)
        X = np.arange(0, 10, 0.2)
        Y = np.arange(0, 10, 0.2)
        X, Y = np.meshgrid(X, Y)
        Z = np.reshape(sombrero([X, Y]), X.shape)

        #plot_surface(linewidth=0) or plot_wireframe
        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, linewidth=0, cmap=cm.jet)

        #fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()

def main():
    sombrero()

if __name__ == '__main__':
    status = main()
