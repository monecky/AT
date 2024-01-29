from abc import ABC, abstractmethod

from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing


class AbstractBu(ABC):
    """
    A class that extends the abstract class such that this format can be used for the other algorithms.
    """

    def __init__(self):
        """Constructor to let the object exist"""
        self.storage_result = {}

    def run_logic(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
        Helper class to reduce duplicate code.
        :param at:  attack tree
        :param node:  node to handle
        :param semi_ring:  the semi ring that is used.
        :param run:  the program where the main program runs in.
        :return: the and or action taken result.
        """
        result = -1
        match node.node_type:
            case NodeType.ROOT_OR:
                result = self.action_ROOT_OR(at, node, semi_ring, run)
            case NodeType.ROOT_AND:
                result = self.action_ROOT_AND(at, node, semi_ring, run)
            case NodeType.OR:
                result = self.action_OR(at, node, semi_ring, run)
            case NodeType.AND:
                result = self.action_AND(at, node, semi_ring, run)
            case NodeType.BAS:
                result = self.action_BAS(at, node, semi_ring, run)
            case _:
                AtError('Not a valid node type.')
        return self.action_AFTER(result, node, at, semi_ring, self.run_dp)

    def run_dp(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the actual algorithm runs, in dynamic programming format.
            :param at: is the attack tree where the security metric needed to be determined over.
            :param node: is the starting point.
            :param semi_ring: is the semi-ring used.
            :return: depends on the algorithm
        """
        if node.node_type == NodeType.ROOT_OR or node.node_type == NodeType.ROOT_AND:
            self.storage_result = {}
        if node in self.storage_result:
            return self.storage_result[node]
        result = self.run_logic(at, node, semi_ring, self.run_dp)
        self.storage_result[node] = result
        return result

    def run(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the actual algorithm runs
            :param at: is the attack tree where the security metric needed to be determined over.
            :param node: is the starting point.
            :param semi_ring: is the semi-ring used.
            :return: depends on the algorithm
        """
        result = self.run_logic(at, node, semi_ring, self.run_dp)
        return result

    @abstractmethod
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
                This where the ROOT_AND logic runs
                :param at: is the attack tree where the security metric needed to be determined over.
                :param node: is the starting point.
                :param semi_ring: is the semi-ring used.
                :param run: methode, where the main program is running in.
                :return: depends on the algorithm
            """
        pass

    @abstractmethod
    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
                This where the ROOT_OR logic runs
                :param at: is the attack tree where the security metric needed to be determined over.
                :param node: is the starting point.
                :param semi_ring: is the semi-ring used.
                :param run: methode, where the main program is running in.
                :return: depends on the algorithm
            """
        pass

    @abstractmethod
    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
            This where the AND logic runs
            :param at: is the attack tree where the security metric needed to be determined over.
            :param node: is the starting point.
            :param semi_ring: is the semi-ring used.
            :param run: methode, where the main program is running in.
            :return: depends on the algorithm
        """
        pass

    @abstractmethod
    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
            This where the OR logic runs
            :param at: is the attack tree where the security metric needed to be determined over.
            :param node: is the starting point.
            :param semi_ring: is the semi-ring used.
            :param run: methode, where the main program is running in.
            :return: depends on the algorithm
        """
        pass

    @abstractmethod
    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing, run):
        """
            This where the BAS logic runs
            :param at: is the attack tree where the security metric needed to be determined over.
            :param node: is the starting point.
            :param semi_ring: is the semi-ring used.
            :param run: methode, where the main program is running in.
            :return: depends on the algorithm
        """
        pass

    @abstractmethod
    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree,  semi_ring: SemiRing, run):
        """
            This where after is done
            :param semi_ring: the operators used.
            :param array_of_numbers: is the output.
            :param node: is the starting point.
            :param at: is the attack tree
            :param run: methode, where the main program is running in.
            :return: depends on the algorithm
        """
        pass
