import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import generation
from all_types import get_config

from args import size, mountain_type

x = [[i for i in range(size[0])] for _ in range(size[1])]
y = [[i for _ in range(size[0])] for i in range(size[1])]
z = generation.generate_mountains(size, get_config(mountain_type))

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, shade=True)
ax.set_zlim([-20, 20])

plt.show()