from src.algorithm.abstractbu import AbstractBu
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.ring.semi_ring import SemiRing


class BuBasis(AbstractBu):
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        result = self.action_AND(at, node, semi_ring)
        return result

    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        result = self.action_OR(at, node, semi_ring)
        return result

    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        ch_v = [self.run(at, child, semi_ring) for child in node.children]
        result = [[0, set(), {}]]
        for u in ch_v:
            w = []
            for bu in u:
                for re in result:
                    delta = bu[1].difference(re[1])
                    new_set = re[1].copy() | bu[1]
                    new_dict = re[2].copy()| bu[2]
                    k = [semi_ring.and_operator([re[0],bu[0],semi_ring.reverse_and(semi_ring.and_operator([new_dict[i] for i in bu[1]])),semi_ring.and_operator([new_dict[i] for i in delta])]),new_set, new_dict]
                    w += [k]
            result = w
        return result

    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        ch_v = [self.run(at, child, semi_ring) for child in node.children]
        result = []
        for u in ch_v:
            result += u
        return result

    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        return [[node.attribute.value, {node}, {node: node.attribute.value}]]

    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree):
        return array_of_numbers

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
