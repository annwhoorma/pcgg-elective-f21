from enum import Enum, auto
from mountain_types import hill, steep, calm

class TileType(Enum):
    '''
    Enum for each existing tile.
    '''
    HILL = auto()
    CALM = auto()
    STEEP = auto() # steep


def get_config(mountype, start_height=20):
    '''
    Creates a configuration for map construction.
    @param mountype: type of the mountain defined by TileType
    @start_height: the starting number on Z axis

    @return a configuration for specified mountain type and height
    '''
    return Configuration(mountype, start_height)


class Configuration:
    '''
    Describes one tile.
    '''
    def __init__(self, mountype, start_height, split=4):
        '''
        @param mountype: type of the mountain defined by TileType
        @start_height: the starting number on Z axis
        @split: a number by which a tile is split into smaller tiles; default is 4
        '''
        self.start, self.values, self.table = None, None, None
        self.mountype = mountype
        self.start_height = start_height
        self.split = split
        # initialize class fields depending on mountain type
        if mountype == TileType.HILL:
            self.start_tile, self.values, self.table = hill.start_tile, hill.values, hill.table
        elif mountype == TileType.STEEP:
            self.start_tile, self.values, self.table =  steep.start_tile, steep.values, steep.table
        elif mountype == TileType.CALM:
            self.start_tile, self.values, self.table =  calm.start_tile, calm.values, calm.table
