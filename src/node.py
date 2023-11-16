from src.nodetype import NodeType
from src.at_error import AtError


class Node(object):
    """
    'Node' objects have a property 'attack_tree' pointing to the AT they are part of,
    and an attribute `label` which can be anything: it is not used for any methods,
    except for `__str__`.
    """

    def __init__(self, vertex_type: NodeType, label=None, color_enum=None, attack_tree=None):
        """
        Creates a node, part of `attack_tree`, with optional label `label`.
        (Labels of different vertices may be chosen the same; this does
        not influence correctness of the methods, but will make the string
        representation of the graph ambiguous.)
        :param attack_tree: The graph that this `Vertex` is a part of
        :param label: Optional parameter to specify a label for the
        """
        if attack_tree is None:
            AtError("A node needs to belong to a graph.")
        if label is None:
            label = attack_tree.next_label()
        if color_enum is None:
            color_enum = 0
        self.color_enum = color_enum
        self.identifier_number_of_vertices = None
        self.identifier_true_or_false = None
        self._at = attack_tree
        self.label = label
        self._incidence = {}
        self.vertex_type = vertex_type

    def __repr__(self):
        """
        A programmer-friendly representation of the node.
        :return: The string to approximate the constructor arguments of the 'Node'
        """
        return 'Node(label={}, #incident={})'.format(self.label, len(self._incidence))

    def __str__(self) -> str:
        """
        A user-friendly representation of the node, that is, its label.
        :return: The string representation of the label.
        """
        return str(self.label)
