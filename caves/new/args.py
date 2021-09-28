from all_types import TileType


start_height = 20
size = (16, 16) # degree of 2
assert size[0] == size[1]
split = 4 # degree of 4

mountain_type = TileType.STEEP
mountain_comb = [
    [TileType.CALM, TileType.HILL, TileType.STEEP],
    [TileType.CALM, TileType.CALM, TileType.HILL],
    [TileType.CALM, TileType.HILL, TileType.STEEP],
    [TileType.CALM, TileType.HILL, TileType.STEEP]
]
