from src.algorithm.bottom_up import bottom_up
from src.algorithm.generateAllMP import gen_bu2
from src.model.ring.semi_ring import MiniumCostMetricTree, MiniumCostMetricGraph
from src.reader.reader import *
from src.algorithm.bottom_up_tree import *
from src.algorithm.generateAllpossibilities import *
import os

def main():
    path = "..\src\example_tree\generate\generate100100100100"
    semi = MetricBasic("int")
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".at"):
            at = get_list_of_at(path+"\\"+filename)[0]
            with open((path+"\\"+filename).replace(".at",".dot"), 'w') as f:
                write_dot(at,f)
            # gen_bu(at,at.root, semi)
            # print(min([bu[0] for bu in gen_bu(at, at.root, semi)]), end=", ")
            # gen_bu2(at,at.root, semi)
            # print(min([bu[0] for bu in gen_bu2(at, at.root, semi)]))
            if min([bu[0] for bu in gen_bu(at, at.root, semi)]) != min([bu[0] for bu in gen_bu2(at, at.root, semi)]):
                print(min([bu[0] for bu in gen_bu(at, at.root, semi)]), end=", ")
                print(min([bu[0] for bu in gen_bu2(at, at.root, semi)]))

            # for i in gen_bu2(at, at.root, semi):
            #     print(i[0])
            #     for node in i[1]:
            #         print(node.label, end=" ")
            #     print()
            #     print(i[2])




if __name__ == "__main__":
    main()
