import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from generation import generate_mountain
from all_types import get_config
import click

from args import size, mountain_type, mountain_comb, start_height, split


def draw_one_mountain(x, y, z, ax, start_height=start_height):
    ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, shade=True)


@click.command()
@click.option('--gen_type', default='1', prompt='Mountain [1] or forest of mountains [2]', type=int)
def main(gen_type: int):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_zlim([-(start_height + 20), start_height+30])

    if gen_type == 1:
        x = [[i for i in range(size[0])] for _ in range(size[1])]
        y = [[i for _ in range(size[0])] for i in range(size[1])]
        config = get_config(mountain_type, start_height, split)
        z = generate_mountain(size, config)
        draw_one_mountain(x, y, z, ax, start_height)
    elif gen_type == 2:
        # configs = [[None for _ in range(len(mountain_comb[0]))] for _ in range(len(mountain_comb))]
        # points = [[None for _ in range(len(mountain_comb[0]))] for _ in range(len(mountain_comb))]
        for i, row in enumerate(mountain_comb):
            for j, mountype in enumerate(row):
                config = get_config(mountype, start_height, split)
                x = [[ii for ii in range(j*size[0], j*size[0]+size[0])] for _ in range(size[1])]
                y = [[ii for _ in range(size[0])] for ii in range(i*size[1], i*size[1]+size[1])]
                z = generate_mountain(size, config)
                draw_one_mountain(x, y, z, ax, start_height)
    else:
        print('incorrect input')
    plt.show()

if __name__ == '__main__':
    main()