from random import choices, randint

from src.model.at.nodetype import NodeType


def generateAT(no_multi_parent:int, max_no: int) -> str:
    """
    The methode attempt to generate attack trees files. In such away we can test the algorithms.
    :param no_multi_parent: gives the number of multi-parents.
    :return str: That needs to be printed in the document.
    """
    result = "" # is the file context
    edges = ""
    or_nodes = str(NodeType.OR.value) + ":"
    and_nodes = str(NodeType.AND.value) + ":"
    root_or_nodes = str(NodeType.ROOT_OR.value) + ":"
    root_and_nodes = str(NodeType.ROOT_AND.value) + ":"
    # Determine the number of BAS, basic attack steps.
    no_bas = randint(2, max_no)
    # Add the BAS to an array
    result += str(NodeType.BAS.value) + ":"
    for i in range(no_bas):
        result += str(i) + "(" + str(randint(2,max_no)) + ","
    result += "\n"
    choices([True,False])
    # Representing the layer of the three
    no_nodes = no_bas
    layer = [i for i in range(no_bas)]



    result += or_nodes +  "\n" +  and_nodes +"\n" +  root_and_nodes + "\n" + root_or_nodes + \
             "\nstop\n" + edges + "\n" + "stop\ndone\n"
    return result