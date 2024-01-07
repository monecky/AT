from src.algorithm.bu_basisMP import BuBasisMP
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node


class BuBasisMPfilter(BuBasisMP):

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, run):
        """
        This methode repeat what is in the action_after class.
        After that it does the following actions:
        1) Each element in array_of_numbers has a unique set.
        2) Additionally only the most optimal value is chosen.
        @param array_of_numbers the option that minium.
        @param node the node where the algorithm is.
        @param at is the attack tree where the metric is calculated from.
        @return the options as specified above.
        """
        array_of_numbers = super().action_AFTER(array_of_numbers, node, at)
        result = []
        for opt in array_of_numbers:
            dirty = True
            for re in result:
                if re[1] == opt[1]:
                    if re[0] > opt[0]:
                        result.remove(re)
                        result.append(opt)
                        dirty = False
                        break
            if dirty:
                result.append(opt)
        array_of_numbers = result
        return array_of_numbers
