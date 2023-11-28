from src.model.ring.semi_ring import MiniumCostMetricTree
from src.reader.reader import *
from src.algorithm.bottom_up_tree import *


def main():
    at = get_list_of_at("..\src\example_tree\\tree1")[0]
    semi = MiniumCostMetricTree("int")
    print(bottom_up_tree(at, at.root, semi))


if __name__ == "__main__":
    main()
