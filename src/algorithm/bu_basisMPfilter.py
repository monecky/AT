from src.algorithm.bu_basisMP import BuBasisMP
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing


class BuBasisMPfilter(BuBasisMP):

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, semi_ring: SemiRing, run):
        """
        This methode repeat what is in the action_after class.
        After that it does the following actions:
        1) Each element in array_of_numbers has a unique set.
        2) Additionally only the most optimal value is chosen.
        :param array_of_numbers: the option that minium.
        :param node: the node where the algorithm is.
        :param at: is the attack tree where the metric is calculated from.
        :return: the options as specified above.
        :param run:  the main methode
        :param semi_ring:  the semi-ring
        """
        array_of_numbers = super().action_AFTER(array_of_numbers, node, at, semi_ring, run)
        array_of_numbers = [c for c in array_of_numbers if all(
            not (c[1] == b[1] and c[2] == b[2]) or (semi_ring.or_operator([c[0], b[0]]) == c[0]) for b in
            array_of_numbers)]
        array_of_numbers = [c for c in array_of_numbers
                            if all(not (c[1].issubset(b[1]) and c[2].issubset(b[2])) or
                                   (semi_ring.or_operator([c[0], b[0]]) == c[0]) for b in array_of_numbers)]
        return array_of_numbers
