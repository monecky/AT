from src.at_error import AtError
from src.node import Node


class Edge(object):
    """
    Edges have properties `tail` and `head` which point to the end nodes
    (`Node` objects). The order of these matters when the graph is directed.
    """

    def __init__(self, tail: Node, head: Node, weight=None):
        """
        Creates an edge between vertices `tail` and `head`
        :param tail: In case the graph is directed, this is the tail of the arrow.
        :param head: In case the graph is directed, this is the head of the arrow.
        :param weight: Optional weight of the node, which can be any type, but usually is a number.
        """
        if tail.at != head.at:
            raise AtError("Can only add edges between nodes of the same graph")

        self._tail = tail
        self._head = head
        self._weight = weight

    def __repr__(self):
        """
        A programmer-friendly representation of the edge.
        :return: The string to approximate the constructor arguments of the 'Edge'
        """
        return 'Edge(head={}, tail={}, weight={})'.format(self.head.label, self.tail.label, self.weight)

    def __str__(self) -> str:
        """
        A user-friendly representation of this edge
        :return: A user-friendly representation of this edge
        """
        return '({}, {})'.format(str(self.tail), str(self.head))

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def weight(self):
        return self._weight
