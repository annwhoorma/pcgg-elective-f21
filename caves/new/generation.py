from mountain_types import steep
from random import choices
from treelib import Node, Tree
from typing import Tuple
import numpy as np

split = 4

def create_root_tile(start):
    root = Tree()
    root.create_node(start, data={'depth': 0, 'increment': start})
    root.leaves()
    return root

def generate_steep(size):
    tiles_tree = create_root_tile(steep.start)

    while len(tiles_tree.leaves()) < size[0] * size[1]:
        for tile in tiles_tree.leaves():
            increments = choices(steep.values, steep.table[tile.data['increment']], k=split)
            new_tiles = [incr + tile.tag for incr in increments]
            for incr, tile_value in zip(increments, new_tiles):
                tiles_tree.create_node(
                    tag=tile_value,
                    parent=tile.identifier,
                    data={'depth': tile.data['depth']+1, 'increment': incr},
                )
    root_node = tiles_tree.get_node(tiles_tree.root)
    mapping = create_empty_matrix(size=2 ** (tiles_tree.depth()))
    center = (2 ** (tiles_tree.depth() - 1), 2 ** (tiles_tree.depth() - 1)) if tiles_tree.depth() > 1 else (1, 1)
    fill_mapping(tiles_tree, root_node, center, mapping)
    mapping = np.array(mapping)#.flatten()
    return mapping


def create_empty_matrix(size):
    return [[0] * size for _ in range(size)]

def jump_level_down(depth, cur_depth):
    return 2**(depth - 2 - cur_depth)

def node_to_square(tree: Tree, node: Node, center: Tuple[int, int], mapping):
    children = tree.children(node.identifier)
    # print('center', center)
    # print('children', [child.tag for child in children])
    # print((center[0]-1, center[1]-1), (center[0]-1, center[1]), (center[0], center[1]-1), (center[0], center[1]))

    mapping[center[0]-1][center[1]-1] = children[0].tag
    mapping[center[0]-1][center[1]] = children[1].tag
    mapping[center[0]][center[1]-1] = children[2].tag
    mapping[center[0]][center[1]] = children[3].tag
    # print(mapping)
    # print('\n')

def fill_mapping(tree: Tree, cur_node: Node, grid_coords: Tuple[int, int], mapping):
    depth = tree.depth()
    cur_depth = cur_node.data['depth']

    jump = jump_level_down(depth, cur_depth)

    jumps = [
        (-jump, -jump),
        (-jump, jump),
        (jump, -jump),
        (jump, jump),
    ]

    if cur_depth < depth - 1:
        for child, jump in zip(tree.children(cur_node.identifier), jumps):
            new_grid_coords = (grid_coords[0] + jump[0], grid_coords[1] + jump[1])
            fill_mapping(tree, child, new_grid_coords, mapping)
    else:
        node_to_square(tree, cur_node, grid_coords, mapping)
    return mapping