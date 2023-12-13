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

    def run(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the actual algorithm runs
            @param at is the attack tree where the security metric needed to be determined over.
            @param node is the starting point.
            @param semi_ring is the semi-ring used.
            @return depends on the algorithm
        """
        result = -1
        match node.node_type:
            case NodeType.ROOT_OR:
                result = self.action_ROOT_OR(at, node, semi_ring)
            case NodeType.ROOT_AND:
                result = self.action_ROOT_AND(at, node, semi_ring)
            case NodeType.OR:
                result = self.action_OR(at, node, semi_ring)
            case NodeType.AND:
                result = self.action_AND(at, node, semi_ring)
            case NodeType.BAS:
                result = self.action_BAS(at, node, semi_ring)
            case _:
                AtError('Not a valid node type.')
        result = self.action_AFTER(result, node, at)
        return result

    @abstractmethod
    def action_ROOT_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
                This where the ROOT_AND logic runs
                @param at is the attack tree where the security metric needed to be determined over.
                @param node is the starting point.
                @param semi_ring is the semi-ring used.
                @return depends on the algorithm
            """
        pass

    @abstractmethod
    def action_ROOT_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
                This where the ROOT_OR logic runs
                @param at is the attack tree where the security metric needed to be determined over.
                @param node is the starting point.
                @param semi_ring is the semi-ring used.
                @return depends on the algorithm
            """
        pass

    @abstractmethod
    def action_AND(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the AND logic runs
            @param at is the attack tree where the security metric needed to be determined over.
            @param node is the starting point.
            @param semi_ring is the semi-ring used.
            @return depends on the algorithm
        """
        pass

    @abstractmethod
    def action_OR(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the OR logic runs
            @param at is the attack tree where the security metric needed to be determined over.
            @param node is the starting point.
            @param semi_ring is the semi-ring used.
            @return depends on the algorithm
        """
        pass

    @abstractmethod
    def action_BAS(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the BAS logic runs
            @param at is the attack tree where the security metric needed to be determined over.
            @param node is the starting point.
            @param semi_ring is the semi-ring used.
            @return depends on the algorithm
        """
        pass

    @abstractmethod
    def action_AFTER(self, array_of_numbers, node: Node, at: AttackTree):
        """
            This where after is done
            @param array_of_numbers is the output.
            @param node is the starting point.
            @param at is the attack tree
            @return depends on the algorithm
        """
        pass
