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

        fig = Figure(figsize=(width, height), dpi=dpi)
        # self.ax = fig.add_subplot(111)
        self.ax1 = fig.add_axes([0.1,0.1,0.8,0.7])
        self.ax2 = fig.add_axes([0.1,0.85,0.8,0.05])
        self.first_time = True

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        # data = [random.random() for i in range(25)]
        # ax = self.figure.add_subplot(111)
        # ax.plot(data, 'r-')

        xlist = np.linspace(-3.0, 3.0, 50)
        print("len(xlist)=",len(xlist))
        ylist = np.linspace(-3.0, 3.0, 50)
        X, Y = np.meshgrid(xlist, ylist)
        Z = np.sqrt(X**2 + Y**2) + 10*np.random.rand()

        # fig, ax = plt.subplots(constrained_layout=True)
        # CS = ax2.contourf(X, Y, Z, 10, cmap=plt.cm.bone, origin=origin)

        # extends = ["neither", "both", "min", "max"]
        cmap = plt.cm.get_cmap("winter")
        levels = [-1.5, -1, -0.5, 0, 0.5, 1]
        #cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extends[0], origin=origin)
        cs = self.ax1.contourf(X, Y, Z, cmap=cmap)
        cbar = plt.colorbar(mappable=cs, cax=self.ax2)
        # self.figure.colorbar(cs, ax=ax, shrink=0.9)
        # self.figure.colorbar(cs, ax=self.cax)

        # self.ax.set_title('contour plot')
        self.draw()
        # plt.clf()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
