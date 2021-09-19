import matplotlib.pyplot as plt
from matplotlib import cm

import numpy as np
import generation

size = (16, 16) # degree of 4
x = [[i for i in range(size[0])] for _ in range(size[1])]
y = [[i for _ in range(size[0])] for i in range(size[1])]
z = generation.generate_steep(size)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, shade=True)
ax.set_zlim([-20, 20])

plt.show()