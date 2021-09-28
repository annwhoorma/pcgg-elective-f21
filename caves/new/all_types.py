from enum import Enum, auto
from mountain_types import hill, steep, calm

class TileType(Enum):
    HILL = auto()
    CALM = auto()
    STEEP = auto() # steep


def get_config(mountype, start_height=20, split=4):
    return Configuration(mountype, start_height, split)


class Configuration:
    def __init__(self, mountype, start_height, split):
        self.start, self.values, self.table = None, None, None
        self.mountype = mountype
        self.start_height = start_height
        self.split = split
        if mountype == TileType.HILL:
            self.start_tile, self.values, self.table = hill.start_tile, hill.values, hill.table
        elif mountype == TileType.STEEP:
            self.start_tile, self.values, self.table =  steep.start_tile, steep.values, steep.table
        elif mountype == TileType.CALM:
            self.start_tile, self.values, self.table =  calm.start_tile, calm.values, calm.table
