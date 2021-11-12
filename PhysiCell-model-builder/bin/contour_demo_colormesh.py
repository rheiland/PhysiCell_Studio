import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
im = ax.pcolormesh(np.array(np.random.rand(2,2) ))
ax.plot(np.cos(np.linspace(0.2,1.8))+0.9, np.sin(np.linspace(0.2,1.8))+0.9, c="k", lw=6)
ax.set_title("Title")
cbar = plt.colorbar(im)
cbar.ax.set_ylabel("Label")


for i in range(5):
    # inside this loop we should not access any variables defined outside
    #   why? no real reason, but questioner asked for it.
    #draw new colormesh
    im = plt.gcf().gca().pcolormesh(np.random.rand(2,2))
    #check if there is more than one axes
    print("# axes = ",len(plt.gcf().axes))
    if len(plt.gcf().axes) > 1: 
        # if so, then the last axes must be the colorbar.
        # we get its extent
        pts = plt.gcf().axes[-1].get_position().get_points()
        # and its label
        label = plt.gcf().axes[-1].get_ylabel()
        # and then remove the axes
        plt.gcf().axes[-1].remove()
        # then we draw a new axes a the extents of the old one
        cax= plt.gcf().add_axes([pts[0][0],pts[0][1],pts[1][0]-pts[0][0],pts[1][1]-pts[0][1]  ])
        # and add a colorbar to it
        cbar = plt.colorbar(im, cax=cax)
        cbar.ax.set_ylabel(label)
        # unfortunately the aspect is different between the initial call to colorbar 
        #   without cax argument. Try to reset it (but still it's somehow different)
        cbar.ax.set_aspect(20)
    else:
        plt.colorbar(im)
    plt.show()

plt.show()
