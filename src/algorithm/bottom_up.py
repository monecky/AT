from typing import List

from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def bottom_up(at: 'AttackTree', root: 'Node', semi_ring: SemiRing):
    result = 0
    match root.node_type:
        case NodeType.ROOT_OR:
            result = semi_ring.root_or_operator([bottom_up(at, child, semi_ring) for child in root.children])
        case NodeType.ROOT_AND:
            result = semi_ring.root_and_operator(([bottom_up(at, child, semi_ring) for child in root.children]))
        case NodeType.OR:
            result = semi_ring.or_operator([bottom_up(at, child, semi_ring) for child in root.children])
        case NodeType.AND:
            result = semi_ring.and_operator(([bottom_up(at, child, semi_ring) for child in root.children]))
        case NodeType.BAS:
            if root.isMultiParent():
                result = [[[root.attribute.value, {root}]], {root: root.attribute.value}]
            else:
                result = [[[root.attribute.value, {}]], {}]
        case _:
            AtError('Not a valid node type.')
    if root.isMultiParent() and root.node_type != NodeType.BAS:
        for sub_result in result:
            sub_result[0][1] += {root}
            sub_result[root] = [result[0]]
    return result
