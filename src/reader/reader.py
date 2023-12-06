"""
Includes functions for reading and writing graphs, in a very simple readable format.
"""
from typing import IO, Tuple

from src.model.at.attack_tree import *

DEFAULT_COLOR_SCHEME = "paired12"
NUM_COLORS = 12


def read_line(f: IO[str]) -> str:
    """
    Read a single non-comment line from a file
    :param f: The file name
    :return: the line
    """
    line = f.readline()

    while len(line) > 0 and line[0] == '#':
        line = f.readline()

    return line


def read_at(f: IO[str]) -> Tuple[AttackTree, List[str], bool]:
    """
    Read a list of attack tree from a file
    :param f: The file where the attack tree is stored.
    :return: The AttackTree
    """
    nodes_list = []
    node_dict = {}
    type_dict = dictAllNodeType()
    while True:
        line = read_line(f)
        if line.count(":") > 0:

            node = line.replace('\n', '').split(":")
            n_type = type_dict[int(node[0])]
            for attr in node[1].split(","):
                if attr != '':
                    if n_type == type_dict[2]:
                        label, weight = attr.split("(")
                    else:
                        label, weight = attr, '0'
                    nodes_list += [Node(n_type, Attribute(int(weight)), int(label))]
                    node_dict[int(label)] = nodes_list[-1]
        elif line == 'stop\n':
            break
    edge_list = []
    while True:
        line = read_line(f)
        if line != 'stop\n':
            edge = line.split(',')
            if len(edge) == 2:
                edge_list += [Edge(node_dict[int(edge[0])], node_dict[int(edge[1])])]
        else:
            break
    return AttackTree(nodes_list, edge_list)



def read_at_list(f: IO[str]) -> Tuple[AttackTree, List[str], bool]:
    """
    Read multiple attack trees of a file
    :param f: The file where the attack tree is stored.
    :return: The AttackTree list
    """
    attack_tree_list = []
    while True:
        attack_tree_list += [read_at(f)]
        if f.readline() == 'done\n':
            break
    return attack_tree_list


def load_at(f: IO[str], read_list: bool) -> 'AttackTree':
    """
    Load a at from a file
    :param f: The file
    :param read_list: Specifies whether to read a list of graphs from the file, or just a single graph.
    :return: The graph, or a list of graphs.
    """
    if read_list:
        at_list = read_at_list(f)
        return at_list
    else:
        at = read_at(f)
        return [at]  # ,options


def get_list_of_at(filename: str) -> 'AttackTree':
    """
    Methode that is called to get a list of attack trees
    @param filename: this is the list of graphs that needs to be handled.
    @return the attack trees that where in the file.
    """
    # open the file
    with open(filename) as f:
        list_of_at = load_at(f, read_list=True)

    return list_of_at
def write_dot(attack_tree: AttackTree, f: IO[str], directed=True):
    """
    Writes a given attack tree to a file in .dot format.
    :param attack_tree: The graph. If its vertices contain attributes `label`, `colortext` or `colornum`, these are also
    included in the file. If its edges contain an attribute `weight`, these are also included in the file.
    :param f: The file.
    :param directed: Whether the graph should be drawn as a directed graph.
    """
    if directed:
        f.write('digraph G {\n')
    else:
        f.write('graph G {\n')

    name = {}
    next_name = 0
    for v in attack_tree.nodes:
        name[v] = next_name
        next_name += 1
        options = 'penwidth=3,'
        if hasattr(v, 'label'):
            options += 'label="' + str(v.label) + '",'
        if hasattr(v, 'colortext'):
            options += 'color="' + v.colortext + '",'
        elif hasattr(v, 'colornum'):
            options += 'color=' + str(v.colornum % NUM_COLORS + 1) + ', colorscheme=' + DEFAULT_COLOR_SCHEME + ','
            if v.colornum >= NUM_COLORS:
                options += 'style=filled,fillcolor=' + str((v.colornum // NUM_COLORS) % NUM_COLORS + 1) + ','
        if hasattr(v,'node_type'):
            if v.node_type == NodeType.OR or v.node_type == NodeType.ROOT_OR:
                options += 'shape = "egg",'
            elif v.node_type != NodeType.BAS:
                options += 'shape = "triangle",'
        if len(options) > 0:
            f.write('    ' + str(name[v]) + ' [' + options[:-1] + ']\n')
        else:
            f.write('    ' + str(name[v]) + '\n')
    f.write('\n')

    for e in attack_tree.edges:
        options = 'penwidth=2,'
        if hasattr(e, 'weight'):
            options += 'label="' + str(e.weight) + '",'
        if hasattr(e, 'colortext'):
            options += 'color="' + e.colortext + '",'
        elif hasattr(e, 'colornum'):
            options += 'color=' + str(e.colornum % NUM_COLORS + 1) + ', colorscheme=' + DEFAULT_COLOR_SCHEME + ','
        if len(options) > 0:
            options = ' [' + options[:-1] + ']'
        if directed:
            f.write('    ' + str(name[e.parent]) + ' -> ' + str(name[e.child]) + options + '\n')
        else:
            f.write('    ' + str(name[e.parent]) + '--' + str(name[e.child]) + options + '\n')

    f.write('}')