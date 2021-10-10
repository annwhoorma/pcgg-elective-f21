'''
Defines user input to the program
'''
from all_types import TileType

# the number on the Z axis for the initial tile(s)
start_height = 20

# size of one tile, degree of 2
size = (16, 16)
assert size[0] == size[1]

# will be used to generate one tile
mountain_type = TileType.HILL

# will be used to generate a forest of tiles
mountain_comb = [
    [TileType.STEEP, TileType.STEEP, TileType.HILL, TileType.CALM, TileType.CALM, TileType.HILL, TileType.STEEP],
    [TileType.HILL, TileType.STEEP, TileType.STEEP, TileType.HILL, TileType.STEEP, TileType.CALM, TileType.CALM],
    [TileType.HILL, TileType.STEEP, TileType.STEEP, TileType.HILL, TileType.HILL, TileType.STEEP, TileType.HILL,],
    [TileType.HILL, TileType.HILL, TileType.HILL, TileType.CALM, TileType.HILL, TileType.STEEP, TileType.HILL,],
    [TileType.CALM, TileType.CALM, TileType.CALM, TileType.CALM, TileType.HILL, TileType.STEEP, TileType.STEEP,],
    [TileType.HILL, TileType.STEEP, TileType.CALM, TileType.CALM, TileType.HILL, TileType.STEEP, TileType.HILL,],
    [TileType.CALM, TileType.HILL, TileType.HILL, TileType.CALM, TileType.CALM, TileType.HILL, TileType.HILL,],
]
