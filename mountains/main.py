import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from generation import generate_mountain
from all_types import get_config
import click
from time import time

from args import size, mountain_type, mountain_comb, start_height


def draw_one_mountain(x, y, z, ax):
    '''
    Plots one tile.
    @param x: 2D array for values on axis x
    @param y: 2D array for values on axis y
    @param z: 2D array for values on axis z
    @param ax: a plot to use
    '''
    ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, shade=True)


# first thing
def flatten_into_one_row(allz):
    zrow = [[] for _ in range(len(allz[0]))]
    for i, rows in enumerate(zip(*allz)):
        for row in rows:
            zrow[i] += row
    return zrow

# second thing
def flatten_into_one(allz):
    zcol = []
    for stash in allz:
        for row in stash:
            zcol.append(row)
    return zcol


@click.command()
@click.option('--gen_type', default='1', prompt='Mountain [1] or forest of mountains [2]', type=int)
def main(gen_type: int):
    '''
    Runs the whole program depending on 'args.py' file and user input.
    @param gen_type: type of generation;
                     1 means to generate one tile, which is specified in 'args.py'
                     2 means to generate an array of tiles, which is specied in 'args.py
    '''
    # create a subplot of set limit on z axis
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_zlim([-(start_height + 40), start_height + 100])

    # for generation of a single tile
    if gen_type == 1:
        # get configuration
        start = time()
        config = get_config(mountain_type, start_height)
        # get x and y (a square if viewed from above)
        x = [[i for i in range(size[0])] for _ in range(size[1])]
        y = [[i for _ in range(size[0])] for i in range(size[1])]
        # generate a mountain depending on the config and size
        z = np.array(generate_mountain(size, config))
        print(f'Time spent for generation: {time() - start}')
        # draw and show the generated mountain
        draw_one_mountain(x, y, z, ax)
        print(f'Time spent for generation and visualization: {time() - start}')

    # for generation of multiple tiles
    elif gen_type == 2:
        allz_col = []
        start = time()
        # iterate over a 2D array of tiles
        for i, row in enumerate(mountain_comb):
            allz_row = []
            # generate a 2D array for Y axis
            for j, mountype in enumerate(row):
                # generate a configuration for the current tile
                config = get_config(mountype, start_height)
                # generate the mountain depending on the config and size
                z = generate_mountain(size, config)
                allz_row.append(z)
            allz_col.append(flatten_into_one_row(allz_row))
        allz = np.array(flatten_into_one(allz_col))
        x = [[i for i in range(len(allz[0]))] for _ in range(len(allz))]
        y = [[i for _ in range(len(allz[0]))] for i in range(len(allz))]

        print(f'Time spent for generation: {time() - start}')

        # draw and show the generated mountain
        draw_one_mountain(x, y, allz, ax)
        print(f'Time spent for generation and visualization: {time() - start}')
    else:
        print('incorrect input')
    plt.show()



if __name__ == '__main__':
    main()

