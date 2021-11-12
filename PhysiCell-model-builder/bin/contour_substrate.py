import sys
import os
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton

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

        # fig = Figure(figsize=(width, height), dpi=dpi)
        # self.ax = fig.add_subplot(111)
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)

        # self.fig, (self.ax0, self.ax1) = plt.subplots(1, 2, figsize=(34, 15), gridspec_kw={'width_ratios': [1.5, 1]})


        self.first_time = True

        self.substrates_toggle = True
        self.cells_toggle = False


        # FigureCanvas.__init__(self, fig)
        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # self.plot()
        self.plot_substrate(0)

    #-----------------------------------------------
    def plot_substrate(self, frame):

        # return

        # print("plot_substrate(): frame*self.substrate_delta_t  = ",frame*self.substrate_delta_t)
        # print("plot_substrate(): frame*self.svg_delta_t  = ",frame*self.svg_delta_t)
        # print("plot_substrate(): fig width: SVG+2D = ",self.figsize_width_svg + self.figsize_width_2Dplot)  # 24
        # print("plot_substrate(): fig width: substrate+2D = ",self.figsize_width_substrate + self.figsize_width_2Dplot)  # 27

        self.title_str = ''

        if self.substrates_toggle:
            if True:  # substrates and 2D plots 
                self.fig, (self.ax0, self.ax1) = plt.subplots(1, 2, figsize=(34, 15), gridspec_kw={'width_ratios': [1.5, 1]})
                # self.ax1_lymph_TC = self.ax1.twinx()
                # self.ax1_lymph_TH2 = self.ax1.twinx()


            # if (self.customized_output_freq and (frame > self.max_svg_frame_pre_therapy)):
            #     self.substrate_frame = self.max_substrate_frame_pre_therapy + (frame - self.max_svg_frame_pre_therapy)
            # else:
            #     self.substrate_frame = int(frame / self.modulo)

            # fname = "output%08d_microenvironment0.mat" % self.substrate_frame
            # xml_fname = "output%08d.xml" % self.substrate_frame

            # full_fname = os.path.join(self.output_dir, fname)
            # full_xml_fname = os.path.join(self.output_dir, xml_fname)

            # if not os.path.isfile(full_fname):
            #     print("Once output files are generated, click the slider.")  # No:  output00000000_microenvironment0.mat
            #     return

            # tree = ET.parse(full_xml_fname)
            # xml_root = tree.getroot()
            # mins = round(int(float(xml_root.find(".//current_time").text)))  # TODO: check units = mins
            # self.substrate_mins= round(int(float(xml_root.find(".//current_time").text)))  # TODO: check units = mins

            # hrs = int(mins/60)
            # days = int(hrs/24)
            # self.title_str = 'substrate: %dd, %dh, %dm' % (int(days),(hrs%24), mins - (hrs*60))
            # self.title_str = 'substrate: %dm' % (mins )   # rwh

            # info_dict = {}
            # scipy.io.loadmat(full_fname, info_dict)
            # M = info_dict['multiscale_microenvironment']
            # f = M[self.field_index, :]   # 4=tumor cells field, 5=blood vessel density, 6=growth substrate

            # try:
            #     xgrid = M[0, :].reshape(self.numy, self.numx)
            #     ygrid = M[1, :].reshape(self.numy, self.numx)
            # except:
            #     print("substrates.py: mismatched mesh size for reshape: numx,numy=",self.numx, self.numy)
            #     pass
#                xgrid = M[0, :].reshape(self.numy, self.numx)
#                ygrid = M[1, :].reshape(self.numy, self.numx)

            xlist = np.linspace(-3.0, 3.0, 50)
            print("len(xlist)=",len(xlist))
            ylist = np.linspace(-3.0, 3.0, 50)
            X, Y = np.meshgrid(xlist, ylist)
            Z = np.sqrt(X**2 + Y**2) + 10*np.random.rand()

            num_contours = 15
            # levels = MaxNLocator(nbins=num_contours).tick_values(self.colormap_min.value, self.colormap_max.value)
            contour_ok = True

            try:
                cmap = plt.cm.get_cmap("winter")
                # substrate_plot = self.ax0.contourf(xgrid, ygrid, M[self.field_index, :].reshape(self.numy,self.numx), num_contours, cmap=self.colormap_dd.value)
                substrate_plot = self.ax0.contourf(X, Y, Z, cmap=cmap)
            except:
                contour_ok = False
                # print('got error on contourf 2.')

            if (contour_ok):
                self.ax0.set_title(self.title_str, fontsize=self.fontsize)
                cbar = self.fig.colorbar(substrate_plot, ax=self.ax0)
                cbar.ax.tick_params(labelsize=self.fontsize)

            self.xmin = -3
            self.xmax = 3
            self.ymin = -3
            self.ymax = 3
            self.ax0.set_xlim(self.xmin, self.xmax)
            self.ax0.set_ylim(self.ymin, self.ymax)

        # Now plot the cells (possibly on top of the substrate)
        # if self.cells_toggle:
        #     if not self.substrates_toggle:
        #         if True:  # cells (SVG), but no 2D plot (and no substrate)
        #             self.fig, (self.ax0, self.ax1) = plt.subplots(1, 2, figsize=(25, self.figsize_height_substrate), gridspec_kw={'width_ratios': [1.1, 1]})
        #             self.ax1_lymph_TC = self.ax1.twinx()
        #             self.ax1_lymph_TH2 = self.ax1.twinx()

        #     self.svg_frame = frame


        # if (self.analysis_data_toggle.value):
        #     self.substrate_frame = int(frame / self.modulo)
        #     self.plot_analysis_data("time", ["assembled_virion"], self.substrate_frame)
        # else:
        #     self.plot_empty_analysis_data()

    #-----------------------------------------------
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
        if self.first_time:
            self.cax = make_axes_locatable(self.ax).append_axes("right", size="5%", pad="2%")
            self.first_time = False
        self.cax.clear()
        self.figure.colorbar(cs, ax=self.cax)

        self.ax.set_title('contour plot')
        self.draw()
        # plt.clf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
