from src.algorithm.abstractbu import AbstractBu
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing
"""
The bottom up algorithm as given for the trees.
"""

class BottomUpTree(AbstractBu):
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return self.action_AND(at, node, semi_ring, run)

    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return self.action_OR(at, node, semi_ring, run)

    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return semi_ring.and_operator([self.run(at, child, semi_ring) for child in node.children])

    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return semi_ring.or_operator([self.run(at, child, semi_ring) for child in node.children])

    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return node.attribute.value

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, run):
        return array_of_numbers
