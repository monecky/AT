from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def bottom_up_tree(at: 'AttackTree', root: 'Node', semi_ring: SemiRing):
    match root.node_type:
        case NodeType.ROOT_OR:
            return semi_ring.or_operator([bottom_up_tree(at, child, semi_ring) for child in root.children], node)
        case NodeType.ROOT_AND:
            return semi_ring.and_operator([bottom_up_tree(at, child, semi_ring) for child in root.children], node)
        case NodeType.OR:
            return semi_ring.or_operator([bottom_up_tree(at, child, semi_ring) for child in root.children], node)
        case NodeType.AND:
            return semi_ring.and_operator([bottom_up_tree(at, child, semi_ring) for child in root.children], node)
        case NodeType.BAS:
            return root.attribute.value
        case _:
            AtError('Not a valid node type.')
