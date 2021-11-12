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

        # fig, ax = plt.subplots()
        # im = ax.pcolormesh(np.array(np.random.rand(2,2) ))
        # ax.plot(np.cos(np.linspace(0.2,1.8))+0.9, np.sin(np.linspace(0.2,1.8))+0.9, c="k", lw=6)
        # ax.set_title("Title")
        # cbar = plt.colorbar(im)
        # cbar.ax.set_ylabel("Label")

        # self.plot()
        xlist = np.linspace(-3.0, 3.0, 50)
        print("len(xlist)=",len(xlist))
        ylist = np.linspace(-3.0, 3.0, 50)
        X, Y = np.meshgrid(xlist, ylist)
        Z = np.sqrt(X**2 + Y**2) + 10*np.random.rand()
        cmap = plt.cm.get_cmap("winter")
        cs = self.ax.contourf(X, Y, Z, cmap=cmap)
        cbar = self.fig.colorbar(cs, ax=self.ax)


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
        cs = self.ax.contourf(X, Y, Z, cmap=cmap)
        # self.figure.colorbar(cs, ax=ax, shrink=0.9)
        # if self.first_time:
        # self.cax.clear()
        # self.cax = make_axes_locatable(self.ax).append_axes("right", size="5%", pad="1%")
            # self.first_time = False
        # self.cax.clear()
        # cbar = self.fig.colorbar(cs, ax=self.cax)
        cbar = self.fig.colorbar(cs, ax=self.ax)
        cbar.ax.tick_params(labelsize=8)
        # cbar.ax.clear()


        print("# axes = ",len(self.fig.axes))
        # im = plt.gcf().gca().pcolormesh(np.random.rand(2,2))
        im = self.fig.gca().pcolormesh(np.random.rand(2,2))

        # print("# axes = ",len(plt.gcf().axes))
        # if len(plt.gcf().axes) > 1: 
        if len(self.fig.axes) > 1: 
            # if so, then the last axes must be the colorbar.
            # we get its extent
            # pts = plt.gcf().axes[-1].get_position().get_points()
            pts = self.fig.axes[-1].get_position().get_points()
            # and its label
            # label = plt.gcf().axes[-1].get_ylabel()
            label = self.fig.axes[-1].get_ylabel()
            # and then remove the axes
            # plt.gcf().axes[-1].remove()
            self.fig.axes[-1].remove()
            # then we draw a new axes a the extents of the old one
            # cax= plt.gcf().add_axes([pts[0][0],pts[0][1],pts[1][0]-pts[0][0],pts[1][1]-pts[0][1]  ])
            cax = self.fig.add_axes([pts[0][0],pts[0][1],pts[1][0]-pts[0][0],pts[1][1]-pts[0][1]  ])
            # and add a colorbar to it
            # cbar = plt.colorbar(im, cax=cax)
            cbar = self.fig.colorbar(im, cax=cax)
            cbar.ax.set_ylabel(label)
            # unfortunately the aspect is different between the initial call to colorbar 
            #   without cax argument. Try to reset it (but still it's somehow different)
            cbar.ax.set_aspect(20)
        else:
            # plt.colorbar(im)
            self.fig.colorbar(im)


        # from app's substrates.py
        # if (contour_ok):
        #     self.ax0.set_title(self.title_str, fontsize=self.fontsize)
        #     cbar = self.fig.colorbar(substrate_plot, ax=self.ax0)
        #     cbar.ax.tick_params(labelsize=self.fontsize)

        # self.ax.set_title('contour plot')
        # self.draw()
        # plt.clf()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
