"""
Includes functions for reading and writing graphs, in a very simple readable format.
"""
import sys
from typing import IO, Tuple, List, Union

from src.model.attack_tree import AttackTree

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
    Read a attack tree from a file
    :param f: The file
    :return: The graph
    """
    options = []

    while True:
        try:
            line = read_line(f)
            n = int(line)
            graph = graphclass(directed=False, n=n)
            break
        except ValueError:
            if len(line) > 0 and line[-1] == '\n':
                options.append(line[:-1])
            else:
                options.append(line)

    line = read_line(f)
    edges = []

    try:
        while True:
            comma = line.find(',')
            if ':' in line:
                colon = line.find(':')
                edges.append((int(line[:comma]), int(line[comma + 1:colon]), int(line[colon + 1:])))
            else:
                edges.append((int(line[:comma]), int(line[comma + 1:]), None))
            line = read_line(f)
    except Exception:
        pass

    indexed_nodes = list(graph.vertices)

    for edge in edges:
        graph += Edge(indexed_nodes[edge[0]], indexed_nodes[edge[1]], edge[2])

    if line != '' and line[0] == '-':
        return graph, options, True
    else:
        return graph, options, False

