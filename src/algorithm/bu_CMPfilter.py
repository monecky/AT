from src.algorithm.bu_basisMPfilter import BuBasisMPfilter
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType


class BuCMPfilter(BuBasisMPfilter):

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree):
        """
        This methode repeat what is in the action_after class.
        After that it does the following actions:
        1) Each element in array_of_numbers has a unique set.
        2) Additionally only the most optimal value is chosen.
        @param array_of_numbers the option that minium.
        @param node the node where the algorithm is.
        @return the options as specified above.
        """
        if node.node_type != NodeType.BAS:
            array_of_numbers = super().action_AFTER(array_of_numbers, node)
            result = array_of_numbers.copy()
            for opt in array_of_numbers:
                dirty = True
                temp = result.copy()
                for re in result:
                    if re[0] > opt[0]:
                        if len(re[1]) < len(opt[1]):
                            if len(opt[1]) == 1:
                                temp.remove(re)
                            else:
                                if re[1].issubset(opt[1]):
                                    temp.remove(re)

                result = temp
            array_of_numbers = result
        return array_of_numbers
