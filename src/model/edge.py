from src.at_error import AtError
from src.node import Node


class Edge(object):
    """
    Edges have properties `tail` and `head` which point to the end nodes
    (`Node` objects). The order of these matters when the graph is directed.
    """

    def __init__(self, parent: Node, child: Node):
        """
        Creates an edge between vertices `tail` and `head`
        :param parent: In case the graph is directed, this is the tail of the arrow.
        :param child: In case the graph is directed, this is the head of the arrow.
        """
        if parent.at != child.at:
            raise AtError("Can only add edges between nodes of the same graph")
        parent.children(child)
        child.parents(parent)
        self._parent = parent
        self._child = child

    def __repr__(self):
        """
        A programmer-friendly representation of the edge.
        :return: The string to approximate the constructor arguments of the 'Edge'
        """
        return 'Edge(parent={}, child={})'.format(self.child.label, self.parent.label)

    def __str__(self) -> str:
        """
        A user-friendly representation of this edge
        :return: A user-friendly representation of this edge
        """
        return '({}, {})'.format(str(self.parent), str(self.child))

    @property
    def child(self):
        return self._child

    @property
    def parent(self):
        return self._parent
