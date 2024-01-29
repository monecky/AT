from src.model.at.edge import *
from src.model.at.node import *
index = 0
"""Attack tree representation"""
class AttackTree(object):
    """
    'AT' objects representation of a complexer hole.
    """
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        """
        Creates a graph.
        :param nodes: Represent the nodes
        :param edges: Represent the edges
        """
        global index
        for node in nodes:
            if node.node_type == NodeType.ROOT_OR or node.node_type == NodeType.ROOT_AND:
                self._root = node
        try:
            if self._root is None:
                AtError("Attack tree needs to contain root")
        except AttributeError:
            AtError("Attack tree needs to contain root")
        self._nodes = nodes
        self._edges = edges
        self.index = index
        index += 1

    def __repr__(self):
        """
        A programmer-friendly representation of the attack tree.
        :return: The string to approximate the constructor arguments of the 'AT'
        """
        return 'Attack tree(Nodes={}, Edges={}, index={})'.format(self.nodes, self.edges, self.index)

    def __str__(self) -> str:
        """
        A user-friendly representation of this attack tree
        :return: A user-friendly representation of this attack tree
        """
        return '({},{}, {})'.format(str(self.index),str(self.nodes), str(self.edges))

    @property
    def root(self):
        return self._root

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges
