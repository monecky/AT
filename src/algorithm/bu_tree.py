from src.algorithm.abstractbu import AbstractBu
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing

"""
The bottom up algorithm as given for the trees.
"""


class BottomUpTree(AbstractBu):
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
          Return the attribute together with the OR operator.
          :param node: the current node
          :param at: the attack tree.
          :param semi_ring: the operators of the attack tree.
          :param run: methode of bu.
          :return: the attribute together with the AND operator.
          """
        return self.action_AND(at, node, semi_ring, run)

    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
           Return the attribute together with the OR operator.
           :param node: the current node
           :param at: the attack tree.
           :param semi_ring: the operators of the attack tree.
           :param run: methode of bu.
           :return: the attribute together with the OR operator.
           """
        return self.action_OR(at, node, semi_ring, run)

    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
          Return the attribute together with the OR operator.
          :param node: the current node
          :param at: the attack tree.
          :param semi_ring: the operators of the attack tree.
          :param run: methode of bu.
          :return: the attribute together with the AND operator.
          """
        return semi_ring.and_operator([self.run(at, child, semi_ring) for child in node.children])

    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
          Return the attribute together with the OR operator.
          :param node: the current node
          :param at: the attack tree.
          :param semi_ring: the operators of the attack tree.
          :param run: methode of bu.
          :return: the attribute together with the OR operator.
          """
        return semi_ring.or_operator([self.run(at, child, semi_ring) for child in node.children])

    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
          Return attribute of the node.
          :param node: the current node
          :param at: the attack tree.
          :param semi_ring: the operators of the attack tree.
          :param run: methode of bu.
          :return: attribute of the node.
          """
        return node.attribute.value

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, run):
        """
        Return array_of_numbers without a change.
        :param array_of_numbers: what is return
        :param node: the current node
        :param at: the attack tree.
        :param run: methode of bu
        :return: array_of_numbers
        """
        return array_of_numbers
