from src.algorithm.bottom_up_basis import BottomUpAll
from src.algorithm.generateAllMP import gen_bu2
from src.model.ring.semi_ring import MiniumCostMetricTree
from src.reader.reader import *
from src.algorithm.bottom_up_tree import *
import os

def main():
    path = "..\src\example_tree\generate\generate100100100100"
    semi = MiniumCostMetricTree("int")
    bottom_up_tree = BottomUpTree()
    bottom_up = BottomUpAll()
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
            if (not (filename.__contains__("23")or filename.__contains__("28") or filename.__contains__("30") or filename.__contains__("35") or filename.__contains__("40"))):
                gen1 = bottom_up.run(at, at.root, semi)
                print(gen1)
                gen2 = bottom_up_tree.run(at, at.root, semi)
                print(gen2)
                # if min([bu[0] for bu in gen1]) != min([bu[0] for bu in gen2]):
                #     print(min([bu[0] for bu in gen1]), end=", ")
                #     print(min([bu[0] for bu in gen2]))
                # else:
                print(filename)

            # for i in gen_bu2(at, at.root, semi):
            #     print(i[0])
            #     for node in i[1]:
            #         print(node.label, end=" ")
            #     print()
            #     print(i[2])




if __name__ == "__main__":
    main()
