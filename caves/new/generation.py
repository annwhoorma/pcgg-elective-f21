from mountain_types import steep
from random import choices
from treelib import Node, Tree
from typing import Tuple

size = (8, 8) # width, height
split = 4

def create_root_tile(start):
    root = Tree()
    root.create_node(start, data={'depth': 0})
    root.leaves()
    return root

def generate_steep(size):
    tiles_tree = create_root_tile(steep.start)

    while len(tiles_tree.leaves()) < size[0] * size[1]:
        for tile in tiles_tree.leaves():
            new_tiles_values = choices(steep.values, steep.table[tile.tag], k=split)
            new_tiles = [val + tile.tag for val in new_tiles_values]
            # print(new_tiles)
            for tile_value in new_tiles:
                tiles_tree.create_node(tag=tile_value, parent=tile.identifier, data={'depth': tile.data['depth']+1})
    # tiles_tree.show()
    return tiles_tree


def create_empty_matrix(size):
    return [[0] * size for _ in range(size)]

def jump_level_down(depth, cur_depth):
    return 2**(depth - 2 - cur_depth)

def node_to_square(tree: Tree, node: Node, center: Tuple[int, int], mapping):
    children = tree.children(node.identifier)
    print('center', center)
    print('children', [child.tag for child in children])
    print((center[0], center[1]), (center[0], center[1]+1), (center[0]+1, center[1]), (center[0]+1, center[1]+1))
    mapping[center[0]][center[1]] = children[0].tag
    mapping[center[0]][center[1]+1] = children[1].tag
    mapping[center[0]+1][center[1]] = children[2].tag
    mapping[center[0]+1][center[1]+1] = children[3].tag
    print(mapping)
    print('\n')

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

# root: tree.get_node(tree.root)

# generate_steep((4, 4))

tree = generate_steep((8, 8))
print([node.tag for node in tree.leaves()])
root_node = tree.get_node(tree.root)
print('\n')
mapping = create_empty_matrix(size=2 ** (tree.depth()))
center = (2 ** (tree.depth() - 2), 2 ** (tree.depth() - 2)) if tree.depth() > 1 else (1, 1)
print(center)
fill_mapping(tree, root_node, center, mapping)
print(mapping)