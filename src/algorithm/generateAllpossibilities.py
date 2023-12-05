from src.model.at.at_error import AtError
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


def gen_bu(at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
    """
    The goal of the methode is to generate a general listwith all possibilities. That are correct options.
    :param at: the attack tree to be analysis
    :param node: which node need to be analysised
    :param semi_ring: the operators that should be used.
    :return: a general list of options.
    """
    result = 0
    match node.node_type:
        case NodeType.OR, NodeType.ROOT_OR:
            result = semi_ring.or_operator([gen_bu(at, child, semi_ring) for child in node.children])
        case NodeType.AND, NodeType.ROOT_AND:
            result = semi_ring.and_operator(([gen_bu(at, child, semi_ring) for child in node.children]))
        case NodeType.BAS:
            if node.isMultiParent():
                result = [[[node.attribute.value, {node}]], {node: node.attribute.value}]
            else:
                result = [[[node.attribute.value, {}]], {}]
        case _:
            AtError('Not a valid node type.')
    if node.isMultiParent() and node.node_type != NodeType.BAS:
        for sub_result in result:
            sub_result[0][1] += {node}
            sub_result[node] = [result[0]]
    return result
class MiniumCostMetricGraph(SemiRing):
    def __init__(self, field):
        self._field = field

    @classmethod
    def root_or_operator(cls, mapping):
        result = cls.or_operator(mapping)
        return min(result[0])[0]

    @classmethod
    def root_and_operator(cls, mapping):
        result = cls.and_operator(mapping)
        return min(result[0])[0]

    @classmethod
    def or_operator(cls, mapping):
        # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[1]
        mapping_value = []
        # We need to check for duplicated and reduce those
        combination_added = []
        for result in mapping:
            combination_added += [result[0][0][1]]
            mapping_value += [result[0][0]]
        result = [cls.thin_out(mapping_value), mapping_attribute]
        return result

    @classmethod
    def and_operator(cls, mapping):
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
        option = cls.thin_out(mapping_value)
        return [option, mapping_attribute]

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
