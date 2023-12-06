from typing import List, Tuple

from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def gen_bu(at: 'AttackTree', node: 'Node', semi_ring: SemiRing) :
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
            result = semi_ring.or_operator([gen_bu(at, child, semi_ring) for child in node.children], node)
        case NodeType.ROOT_AND:
            result = semi_ring.and_operator([gen_bu(at, child, semi_ring) for child in node.children], node)
        case NodeType.OR:
            result = semi_ring.or_operator([gen_bu(at, child, semi_ring) for child in node.children], node)
        case NodeType.AND:
            result = semi_ring.and_operator([gen_bu(at, child, semi_ring) for child in node.children], node)
        case NodeType.BAS:
            result = [[node.attribute.value, {node}, {node: node.attribute.value}]]
        case _:
            AtError('Not a valid node type.')
    if isinstance(node, AttackTree):
        AtError('No NodeType')
    return result


class MetricBasic(SemiRing):
    def __init__(self, field):
        self._field = field

    @classmethod
    def root_or_operator(cls, mapping, node):
        result = cls.or_operator(mapping, node)
        return min(result[0])[0]

    @classmethod
    def root_and_operator(cls, mapping, node):
        result = cls.and_operator(mapping, node)
        return min(result[0])[0]

    @classmethod
    def or_operator(cls, ch_v, current_node: Node):
        result = []
        for u in ch_v:
            for bu in u:
                # Iterating through all options
                # That is because the effect of choice this path.
                result += [bu]
        return result

    @classmethod
    def and_operator(cls,options, current_node: Node):
        result = [[0, set(), {}]]
        for ch_v in options:
            if ch_v == 0:
                return 0
            w =[]
            for u in ch_v:
                for re in result:
                    k = [re[0], re[1].copy(), re[2].copy()]
                    k[0] += u[0]
                    for n in u[1]:
                        if n in k[1]:
                            k[0] -= u[2][n]
                        else:
                            k[1].add(n)
                            k[2][n] = u[2][n]
                    w += [k]
            result = w
        return result

    @staticmethod
    def thin_out(mapping_value):
        # Thin out options, by choosing the smallest with the nodes.
        option = []
        for change in mapping_value:
            add = True
            for found in option:
                if found[1] == change[1]:
                    add = False
                    if found[0] > change[0]:
                        option.remove(found)
                        option.append(change)
            if add:
                option += [change]
        return option
