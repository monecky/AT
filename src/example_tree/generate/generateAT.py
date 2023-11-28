from math import floor
from random import choices, randint, random

from src.model.at.nodetype import NodeType


def generateAT(no_multi_parent: int, max_no_bas: int, max_weight: int) -> str:
    """
    The methode attempt to generate attack trees files. In such away we can test the algorithms.
    :param no_multi_parent: gives the number of multi-parents.
    :param max_no_bas: maximum of number of BAS basic attacks.
    :param max_weight: maximum weight of the nodes.
    :return str: That needs to be printed in the document.
    """
    result = ""  # is the file context
    edges = ""
    or_nodes = str(NodeType.OR.value) + ":"
    and_nodes = str(NodeType.AND.value) + ":"
    root_or_nodes = str(NodeType.ROOT_OR.value) + ":"
    root_and_nodes = str(NodeType.ROOT_AND.value) + ":"
    # Determine the number of BAS, basic attack steps.
    no_bas = randint(2, max_no_bas)
    # Add the BAS to an array
    result += str(NodeType.BAS.value) + ":"
    for i in range(no_bas):
        result += str(i) + "(" + str(randint(2, max_weight)) + ","
    result += "\n"
    choices([True, False])
    # Representing the layer of the three
    layer = [i for i in range(no_bas)]
    # Track of how many nodes there are
    no_nodes = no_bas
    # Track of how many multiple parents nodes there are
    no_mp = no_multi_parent
    # Keep track of edges that are added
    track_edges = []
    # Adding more nodes until 1 node needs to be generated make that root.
    while len(layer) != 1:  # not if max_no
        if no_mp:
            decision_mp = choices([True, False])
            if decision_mp:
                no_mp = no_mp - 1
                layer += [layer[randint(0, len(layer) - 1)]]  # Adding the node with mp to the layer as addition.
        # Deciding how many nodes need to be combined in the layer
        comb_node = biased_random(2, len(layer))
        or_or_and = choices([True, False])
        # Check for ROOT node
        if comb_node == len(layer):
            if or_or_and[0]:
                root_or_nodes += str(no_nodes) + ","
            else:
                root_and_nodes += str(no_nodes) + ","
        else:
            if or_or_and[0]:
                or_nodes += str(no_nodes) + ","
            else:
                and_nodes += str(no_nodes) + ","
        for i in range(comb_node):
            remove_node = randint(0, len(layer) - 1)  # Decide which node to remove and to be added
            if [no_nodes, layer[remove_node]] not in track_edges:
                edges += str(no_nodes) + "," + str(layer[remove_node]) + "\n"
                track_edges += [[no_nodes, layer[remove_node]]]
            layer.remove(layer[remove_node])
        layer += [no_nodes]
        # Put the counter further
        no_nodes += 1

    result += or_nodes + "\n" + and_nodes + "\n" + root_and_nodes + "\n" + root_or_nodes + "\nstop\n"
    result += edges + "\nstop\ndone\n"
    return result


def biased_random(minim: int, maxim: int):
    return floor(abs(random() - random()) * (1 + maxim - minim) + minim)

