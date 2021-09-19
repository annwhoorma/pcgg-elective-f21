from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import generation

## Create a GL View widget to display data
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('pyqtgraph example: GLSurfacePlot')
w.setCameraPosition(distance=50)

g = gl.GLGridItem()
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

size = (16, 16)
x, y = np.zeros(size), np.zeros(size)
z = generation.generate_steep(size)
print(x)
print(y)
z = np.array(z)
print(z)
points = np.column_stack((x, y, z))
# mountain = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
mountain = gl.GLScatterPlotItem(pos=points)
w.addItem(mountain)


timer = QtCore.QTimer()
timer.start(30)

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()