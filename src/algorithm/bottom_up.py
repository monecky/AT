from typing import List

from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.attribute import Attribute
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def bottom_up_tree(at: 'AttackTree', root: 'Node', semi_ring: SemiRing):
    result = 0
    match root.node_type:
        case NodeType.ROOT_OR:
            result = semi_ring.or_operator([bottom_up_tree(at, child, semi_ring) for child in root.children])
        case NodeType.ROOT_AND:
            result = semi_ring.and_operator(([bottom_up_tree(at, child, semi_ring) for child in root.children]))
        case NodeType.OR:
            result = semi_ring.or_operator([bottom_up_tree(at, child, semi_ring) for child in root.children])
        case NodeType.AND:
            result = semi_ring.and_operator(([bottom_up_tree(at, child, semi_ring) for child in root.children]))
        case NodeType.BAS:
            if root.isMultiParent():
                result = [[root.attribute.value, [root]], [root, root.attribute.value]]
            else:
                result = [[root.attribute.value, []], [root, root.attribute.value]]
        case _:
            AtError('Not a valid node type.')
    if root.isMultiParent():
        #TODO
        map_mp[root] = result
    return result
