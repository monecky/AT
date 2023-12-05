from src.algorithm.bottom_up import bottom_up
from src.model.ring.semi_ring import MiniumCostMetricTree, MiniumCostMetricGraph
from src.reader.reader import *
from src.algorithm.bottom_up_tree import *
from src.algorithm.generateAllpossibilities import *

def main():
    at = get_list_of_at("..\src\example_tree\\treeCAND")[0]
    # semi = MiniumCostMetricTree("int")
    # print(bottom_up_tree(at, at.root, semi))
    semi = MetricBasic("int")
    print(gen_bu(at, at.root,semi))
    for i in gen_bu(at, at.root, semi):
        print(i[0])
        for node in i[1]:
            print(node.label, end=" ")
        print()
        print(i[2])


if __name__ == "__main__":
    main()
