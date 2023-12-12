from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing

def gen_bu2(at: 'AttackTree', node: 'Node', semi_ring: SemiRing) :
    """
    The goal of the methode is to generate a general list with all possibilities. That are correct options.
    :param at: the attack tree to be analysis
    :param node: which node need to be analysis
    :param semi_ring: the operators that should be used.
    :return: a general list of options. : List[List[int, set[Node], dict[Node: int]]]
    """
    result = 0
    match node.node_type:
        case NodeType.ROOT_OR:
            result = semi_ring.or_operator([gen_bu2(at, child, semi_ring) for child in node.children], node)
        case NodeType.ROOT_AND:
            result = semi_ring.and_operator([gen_bu2(at, child, semi_ring) for child in node.children], node)
        case NodeType.OR:
            result = semi_ring.or_operator([gen_bu2(at, child, semi_ring) for child in node.children], node)
        case NodeType.AND:
            result = semi_ring.and_operator([gen_bu2(at, child, semi_ring) for child in node.children], node)
        case NodeType.BAS:
            result = [[node.attribute.value, set(), dict()]]
        case _:
            AtError('Not a valid node type.')
    if not isinstance(node, Node):
        AtError('No NodeType')
    if node.isMultiParent():
        for re in result:
            alpha = re[0]
            for n in re[1]:
                alpha = alpha - re[2][n]
            if alpha != 0:
                re[1].add(node)
                re[2][node] = alpha
    return result