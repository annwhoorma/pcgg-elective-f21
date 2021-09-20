from random import choices
from treelib import Node, Tree
from typing import Tuple
import numpy as np
from all_types import MountainType
from mountain_types import steep, volcano

split = 4

def create_root_tile(start_value, start_tile):
    root = Tree()
    root.create_node(start_value, data={'depth': 0, 'increment': start_tile})
    root.leaves()
    return root

def generate_mountains(size, config):
    tiles_tree = create_root_tile(config.start_value, config.start_tile)
    if config.mountype == MountainType.STEEP:
        __generate_steep__(size, config, tiles_tree)
    elif config.mountype == MountainType.VOLCANO:
        __generate_volcano__(size, config, tiles_tree)

    root_node = tiles_tree.get_node(tiles_tree.root)
    mapping = __create_empty_matrix__(size=2 ** (tiles_tree.depth()))
    center = (2 ** (tiles_tree.depth() - 1), 2 ** (tiles_tree.depth() - 1)) if tiles_tree.depth() > 1 else (1, 1)
    __fill_mapping__(tiles_tree, root_node, center, mapping)
    mapping = np.array(mapping)
    return mapping


def __generate_steep__(size, config, tiles_tree):
    while len(tiles_tree.leaves()) < size[0] * size[1]:
        for tile in tiles_tree.leaves():
            increments = choices(config.values, config.table[tile.data['increment']], k=split)
            new_tiles = [incr + tile.tag for incr in increments]
            for incr, tile_value in zip(increments, new_tiles):
                tiles_tree.create_node(
                    tag=tile_value,
                    parent=tile.identifier,
                    data={'depth': tile.data['depth']+1, 'increment': incr},
                )


def __generate_volcano__(size, config, tiles_tree):
    thresh = 0
    while len(tiles_tree.leaves()) < size[0] * size[1]:
        for tile in tiles_tree.leaves():
            if thresh < config.threshold:
                increments = choices(config.values, config.table_before[tile.data['increment']], k=split)
            else:
                increments = choices(config.values, config.table_after[tile.data['increment']], k=split)
            new_tiles = [incr + tile.tag for incr in increments]
            for incr, tile_value in zip(increments, new_tiles):
                tiles_tree.create_node(
                    tag=tile_value,
                    parent=tile.identifier,
                    data={'depth': tile.data['depth']+1, 'increment': incr},
                )
        thresh += 1


def __create_empty_matrix__(size):
    return [[0] * size for _ in range(size)]

def __jump_level_down__(depth, cur_depth):
    return 2**(depth - 2 - cur_depth)

def __node_to_square__(tree: Tree, node: Node, center: Tuple[int, int], mapping):
    children = tree.children(node.identifier)

    mapping[center[0]-1][center[1]-1] = children[0].tag
    mapping[center[0]-1][center[1]] = children[1].tag
    mapping[center[0]][center[1]-1] = children[2].tag
    mapping[center[0]][center[1]] = children[3].tag


def __fill_mapping__(tree: Tree, cur_node: Node, grid_coords: Tuple[int, int], mapping):
    depth = tree.depth()
    cur_depth = cur_node.data['depth']

    jump = __jump_level_down__(depth, cur_depth)

    jumps = [
        (-jump, -jump),
        (-jump, jump),
        (jump, -jump),
        (jump, jump),
    ]

    if cur_depth < depth - 1:
        for child, jump in zip(tree.children(cur_node.identifier), jumps):
            new_grid_coords = (grid_coords[0] + jump[0], grid_coords[1] + jump[1])
            __fill_mapping__(tree, child, new_grid_coords, mapping)
    else:
        __node_to_square__(tree, cur_node, grid_coords, mapping)
    return mapping