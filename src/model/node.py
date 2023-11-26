from src.model.attribute import *
from src.model.nodetype import *
from src.model.at_error import *


class Node(object):
    """
    'Node' objects have a property 'attack_tree' pointing to the AT they are part of,
    and an attribute `label` which can be anything: it is not used for any methods,
    except for `__str__`.
    """

    def __init__(self, node_type: NodeType, attribute: 'Attribute', label=None, color_enum=None, attack_tree=None):
        """
        Creates a node, part of `attack_tree`, with optional label `label`.
        (Labels of different vertices may be chosen the same; this does
        not influence correctness of the methods, but will make the string
        representation of the graph ambiguous.)
        :param attack_tree: The graph that this `Vertex` is a part of
        :param label: Optional parameter to specify a label for the
        """
        if color_enum is None:
            color_enum = 0
        self._color_enum = color_enum
        self._at = attack_tree
        self._label = label
        self._parents = []
        self._children = []
        self._node_type = node_type
        self._attribute = attribute

    def __repr__(self):
        """
        A programmer-friendly representation of the node.
        :return: The string to approximate the constructor arguments of the 'Node'
        """
        return 'Node(label={}, #parents={}, #children={}, #attribute={})'.format(self.label, len(self.parents),
                                                                                 len(self.children), self._attribute)

    def __str__(self) -> str:
        """
        A user-friendly representation of the node, that is, its label.
        :return: The string representation of the label.
        """
        return str(self.label)

    @property
    def at(self):
        return self._at

    @property
    def label(self):
        return self._label

    @property
    def node_type(self):
        return self._node_type

    @property
    def parents(self):
        return self._parents

    @property
    def children(self):
        return self._children

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, attribute: 'attribute'):
        self._attribute = attribute

    @at.setter
    def at(self, attack_tree=None):
        if attack_tree is None:
            AtError("A node needs to belong to a graph.")
        self._at = attack_tree

    @label.setter
    def label(self, label: int):
        self._label = label

    @node_type.setter
    def node_type(self, node_type: 'NodeType'):
        self._node_type = node_type

    @parents.setter
    def parents(self, parent: 'Node'):
        self._parents += [parent]

    @children.setter
    def children(self, children: 'Node'):
        self._children += [children]
