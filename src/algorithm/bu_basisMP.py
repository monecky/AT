from src.algorithm.bu_basis import BuBasis
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing


class BuBasisMP(BuBasis):
    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        return [[node.attribute.value, set(), dict()]]

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree, run):
        if node.isMultiParent():
            for re in array_of_numbers:
                alpha = re[0]
                for n in re[1]:
                    alpha = alpha - re[2][n]
                if alpha != 0:
                    re[1].add(node)
                    re[2][node] = alpha
        return array_of_numbers
