from src.algorithm.bu_CMPfilter import BuCMPfilter
from src.algorithm.bu_basisMP import BuBasisMP
from src.model.at.at_error import AtError
from src.model.at.attack_tree import AttackTree
from src.model.at.node import Node
from src.model.at.nodetype import NodeType
from src.model.ring.semi_ring import SemiRing

subSolution = {}
class dy_CMPfilter(BuBasisMP):
    def run(self, at: 'AttackTree', node: 'Node', semi_ring: SemiRing):
        """
            This where the actual algorithm runs
            @param at is the attack tree where the security metric needed to be determined over.
            @param node is the starting point.
            @param semi_ring is the semi-ring used.
            @return depends on the algorithm
        """
        global subSolution
        result = -1
        match node.node_type:
            case NodeType.ROOT_OR:
                subSolution = {}
                result = self.action_ROOT_OR(at, node, semi_ring)
                result = self.action_AFTER(result, node, at)
            case NodeType.ROOT_AND:
                subSolution = {}
                result = self.action_ROOT_AND(at, node, semi_ring)
                result = self.action_AFTER(result, node, at)
            case NodeType.OR:
                if node in subSolution:
                    result = subSolution[node]
                else:
                    result = self.action_OR(at, node, semi_ring)
                    result = self.action_AFTER(result, node, at)
            case NodeType.AND:
                if node in subSolution:
                    result = subSolution[node]
                else:
                    result = self.action_AND(at, node, semi_ring)
                    result = self.action_AFTER(result, node, at)
            case NodeType.BAS:
                if node in subSolution:
                    result = subSolution[node]
                else:
                    result = self.action_BAS(at, node, semi_ring)
                    result = self.action_AFTER(result, node, at)
            case _:
                AtError('Not a valid node type.')

        subSolution[node] = result
        return result
