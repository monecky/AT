from src.algorithm.bu_basis import BuBasis
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing

"""BuMp algorithm from the paper"""


class BuBasisMP(BuBasis):
    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
        returns a triple with attribute value
        :param at: the attack tree
        :param node: the node that is considered
        :param semi_ring: the semi-ring that is used
        :param run: the bottom-up algorithm that is used.
        :return: a triple with attribute value on place.
        """
        return [[node.attribute.value, set(), dict()]]

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, run):
        """
        add if necessary the mp
        :param array_of_numbers: result
        :param node:  node that is considered
        :param at: the attack tree
        :param run: the bottom-up algorithm
        :return: the mp is added if node is mp, to each triple.
        """
        if node.isMultiParent():
            for re in array_of_numbers:
                alpha = re[0]
                for n in re[1]:
                    alpha = alpha - re[2][n]
                if alpha != 0:
                    re[1].add(node)
                    re[2][node] = alpha
        return array_of_numbers
