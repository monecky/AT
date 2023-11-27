"""
Includes functions for reading and writing graphs, in a very simple readable format.
"""
from typing import IO, Tuple

from src.model.attack_tree import *

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
    Read an attack tree from a file
    :param f: The file where the attack tree is located
    :return: The AttackTree
    """
    node_types = allNodeType()
    for node_type in node_types:
        line = read_line(f)
        if (line.find(":")):
            node = line.split(":")
            print(node)
            node_type.value
    return [AttackTree([Node(node_type.ROOT_AND, Attribute(0))], [])]


def read_at_list(f: IO[str]) -> Tuple[AttackTree, List[str], bool]:
    """
    Read a list of attack tree from a file
    :param f: The file where the attack tree is stored.
    :return: The AttackTree list
    """
    print("read list for advance")
    nodes_list = []
    node_dict = dictAllNodeType()
    while True:
        line = read_line(f)
        print(line)
        if line.count(":")>0:

            node = line.replace('\n','').split(":")
            n_type = node_dict[int(node[0])]
            for attr in node[1].split(","):
                if attr == '':
                    break
                elif n_type == node_dict[2]:
                    label, weight = attr.split("(")
                else:
                    label, weight = attr, '0'
                print(label)
                print(weight)
                nodes_list += [Node(n_type,Attribute(int(weight)), int(label))]

            print(node)
        else:
            break

    return [AttackTree([Node(allNodeType()[0].ROOT_AND, Attribute(0))], [])]


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
        return at  # ,options


def get_list_of_at(filename: str) -> 'AttackTree':
    """
    Methode that is called to get a list of attack trees
    @param filename: this is the list of graphs that needs to be handled.
    @return the attack trees that where in the file.
    """
    # open the file
    with open(filename) as f:
        list_of_at = load_at(f, read_list=True)

    # Give all the graphs an index, which represents the index in the initial list
    i = 0
    for at in list_of_at:
        at.index = i
        i += 1

    return list_of_at
