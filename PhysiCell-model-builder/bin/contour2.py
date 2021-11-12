import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import numpy as np

a = np.arange(10)
bb, cc = np.meshgrid(a, a)
u = np.random.randint(2, 4, (10, 10))
v = np.random.randint(2, 4, (10, 10))

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)

# create axes for the colorbar
cax = make_axes_locatable(ax).append_axes("right", size="5%", pad="2%")


for i in range(10):
    # clear colorbar axes
    cax.clear()
    u = np.random.randint(2, 4, (10, 10))
    v = np.random.randint(2, 4, (10, 10))
    ws = np.sqrt(u**2 + v**2)

    cf = ax.contourf(bb, cc, ws)
    # draw new colorbar in existing cax
    cb = fig.colorbar(cf, cax=cax)

    fig.canvas.update()
    fig.canvas.flush_events()

    #plt.savefig('test_barb/%i.png' % i, dpi=200)


plt.show()
