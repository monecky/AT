
from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def bottom_up(at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
    """
    The goal of the methode is the determine the security metrics.
    :param at: 
    :param node:
    :param semi_ring:
    :return:
    """
    result = 0
    match node.node_type:
        case NodeType.ROOT_OR:
            result = semi_ring.root_or_operator([bottom_up(at, child, semi_ring) for child in node.children], node)
        case NodeType.ROOT_AND:
            result = semi_ring.root_and_operator(([bottom_up(at, child, semi_ring) for child in node.children]), node)
        case NodeType.OR:
            result = semi_ring.or_operator([bottom_up(at, child, semi_ring) for child in node.children], node)
        case NodeType.AND:
            result = semi_ring.and_operator(([bottom_up(at, child, semi_ring) for child in node.children]), node)
        case NodeType.BAS:
            if node.isMultiParent():
                result = [[[node.attribute.value, {node}]], {node: node.attribute.value}]
            else:
                result = [[[node.attribute.value, {}]], {}]
        case _:
            AtError('Not a valid node type.')
    if node.isMultiParent() and node.node_type != NodeType.BAS:
        for sub_result in result:
            sub_result[0][1] += {node}
            sub_result[node] = [result[0]]
    return result
