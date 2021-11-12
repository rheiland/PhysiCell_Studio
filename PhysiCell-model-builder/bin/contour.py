import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
# from PyQt5.QtGui import QIcon


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable


import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'PyQt5 matplotlib example - pythonspot.com'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.m = PlotCanvas(self, width=5, height=4)
        self.m.move(0,0)

        button = QPushButton('Redraw', self)
        button.setToolTip('This s an example button')
        button.clicked.connect(self.redraw)
        button.move(500,0)
        button.resize(140,100)

        self.show()

    def redraw(self):
        print("----- redraw")
        # self.m.plot1D()
        self.m.plot()


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        # self.first_time = True

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # self.plot()
        xlist = np.linspace(-3.0, 3.0, 50)
        print("len(xlist)=",len(xlist))
        ylist = np.linspace(-3.0, 3.0, 50)
        X, Y = np.meshgrid(xlist, ylist)
        Z = np.sqrt(X**2 + Y**2) + 10*np.random.rand()

        self.cmap = plt.cm.get_cmap("winter")
        self.cs = self.ax.contourf(X, Y, Z, cmap=self.cmap)
        self.cbar = self.fig.colorbar(self.cs, ax=self.ax)


    def plot(self):
        # data = [random.random() for i in range(25)]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-')

        xlist = np.linspace(-3.0, 3.0, 50)
        print("len(xlist)=",len(xlist))
        ylist = np.linspace(-3.0, 3.0, 50)
        X, Y = np.meshgrid(xlist, ylist)
        Z = np.sqrt(X**2 + Y**2) + 10*np.random.rand()
        cs = self.ax.contourf(X, Y, Z, cmap=self.cmap)

        print("# axes = ",len(self.fig.axes))
        if len(self.fig.axes) > 1: 
            pts = self.fig.axes[-1].get_position().get_points()
            label = self.fig.axes[-1].get_ylabel()
            self.fig.axes[-1].remove()
            cax = self.fig.add_axes([pts[0][0],pts[0][1],pts[1][0]-pts[0][0],pts[1][1]-pts[0][1]  ])
            self.cbar = self.fig.colorbar(cs, cax=cax)
            self.cbar.ax.set_ylabel(label)

            # unfortunately the aspect is different between the initial call to colorbar 
            #   without cax argument. Try to reset it (but still it's somehow different)
            self.cbar.ax.set_aspect(20)
        else:
            # plt.colorbar(im)
            self.fig.colorbar(cs)

        self.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
