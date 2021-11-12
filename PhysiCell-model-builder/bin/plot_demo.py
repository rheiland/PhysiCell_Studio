import sys
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
# from PyQt5.QtGui import QIcon


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import scipy.stats


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
        self.ax = fig.add_subplot(111)
        self.first_time = True

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        x = np.linspace(1,2, 100)
        X, Y = np.meshgrid(x, x)
        # Z = plt.mlab.bivariate_normal(X,Y,1,1,0,0)

        # Z = matplotlib.mlab.bivariate_normal(X, Y, sig_x, sig_y, mu_x, mu_y, sig_xy)
        rv = scipy.stats.multivariate_normal([0, 0], [[1, 1], [1, 1]])
        Z = rv.pdf(np.dstack((X, Y)))

        fig = plt.figure()
        ax1 = fig.add_axes([0.1,0.1,0.8,0.7])
        ax2 = fig.add_axes([0.1,0.85,0.8,0.05])

        for i in range(1,5):
            plotted = ax1.pcolor(X,Y,Z)
            cbar = plt.colorbar(mappable=plotted, cax=ax2, orientation = 'horizontal')
            #note "cax" instead of "ax"
            # plt.savefig(os.path.expanduser(os.path.join('~/', str(i))))
            plt.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
