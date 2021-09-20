from enum import Enum, auto
from mountain_types import steep, volcano

class MountainType(Enum):
    STEEP = auto()
    VOLCANO = auto()

def get_config(mountype):
    return Configuration(mountype)

class Configuration:
    def __init__(self, mountype):
        self.start, self.values, self.table, self.threshold = None, None, None, None
        self.mountype = mountype
        if mountype == MountainType.STEEP:
            self.start_tile, self.values, self.table = steep.start_tile, steep.values, steep.table
            self.start_value = steep.start_value
        elif mountype == MountainType.VOLCANO:
            self.start_tile, self.values =  volcano.start_tile, volcano.values
            self.table_before, self.table_after = volcano.table_before, volcano.table_after
            self.threshold = volcano.threshold
            self.start_value = volcano.start_value