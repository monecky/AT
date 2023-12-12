from src.algorithm.abstractbu import AbstractBu
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


class BottomUp(AbstractBu):
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        result = self.action_AND(at, node, semi_ring)
        return semi_ring.and_operator(result[0])[0]

    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        result = self.action_OR(at, node, semi_ring)
        return semi_ring.or_operator(result[0])[0]

    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        mapping = ([self.run(at, child, semi_ring) for child in node.children])
        # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[1]
        # Reduce result.
        added_nodes = []
        # Adding for the min/max
        for result in mapping:
            for node in result[0][1]:
                if node not in added_nodes:
                    added_nodes += [node]
                    ''''Adding all possibilities together'''
        option = []  # list of options
        new_option = []
        for result in mapping:
            if len(option) == 0:
                option = result[0]
            else:
                for path in result[0]:
                    for change in option:
                        element = change.copy()
                        element[0] += path[0]
                        for node in path[1]:
                            if node not in change[1]:
                                element[1] = set(element[1]) | {node}
                            else:
                                element[0] -= mapping_attribute[node]
                        new_option += [element]
                option = new_option
                new_option = []
        mapping_value = option
        # Thin out options
        option = self.thin_out(mapping_value, node)
        return [option, mapping_attribute]

    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        mapping = ([self.run(at, child, semi_ring) for child in node.children])  # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[1]
        mapping_value = []
        # We need to check for duplicated and reduce those
        combination_added = []
        for result in mapping:
            combination_added += [result[0][0][1]]
            mapping_value += [result[0][0]]
        result = [self.thin_out(mapping_value, node), mapping_attribute]
        return result

    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        if node.isMultiParent():
            result = [[[node.attribute.value, {node}]], {node: node.attribute.value}]
        else:
            result = [[[node.attribute.value, {}]], {}]
        return result

    def action_AFTER(self, array_of_numbers, node):
        if node.isMultiParent() and node.node_type != NodeType.BAS:
            for sub_result in array_of_numbers:
                sub_result[0][1] += {node}
                sub_result[node] = [array_of_numbers[0]]
        return array_of_numbers

    @staticmethod
    def thin_out(mapping_value, node):
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
