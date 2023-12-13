from src.algorithm.bu_CMPfilter import BuCMPfilter
from src.algorithm.bu_basis import BuBasis
from src.algorithm.bu_basisMP import BuBasisMP
from src.algorithm.bu_basisMPfilter import BuBasisMPfilter
from src.algorithm.dy_CMPfilter import dy_CMPfilter
from src.model.ring.semi_ring import MiniumCostMetricTree
from src.reader.reader import *
from src.algorithm.bu_tree import *
import os

def main():
    path = "..\src\example_tree\generate\generate100100100100"
    semi = MiniumCostMetricTree("int")
    bottom_up_tree = BottomUpTree()
    bottom_up = BuBasis()
    bottom_up_mp = BuBasisMP()
    bu_Bmp_filter = BuBasisMPfilter()
    bu_Cmp_filter = BuCMPfilter()
    dynamic = dy_CMPfilter()

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
            if (not (filename.__contains__("23") or filename.__contains__("28") or filename.__contains__("30") or filename.__contains__("35") or filename.__contains__("40")or filename.__contains__("47")or filename.__contains__("49"))):
            # if True:
                # basis = bottom_up.run(at, at.root, semi)
                # print(min(basis))
                # basisMP = bottom_up_mp.run(at, at.root, semi)
                # print(min(basisMP))
                basisMPf = bu_Bmp_filter.run(at, at.root, semi)
                # print(min(basisMPf))
                buD = dynamic.run(at, at.root, semi)
                # print(min(CMPf))
                # gen2 = bottom_up_tree.run(at, at.root, semi)
                # print(gen2)
                # if gen2 > min(basisMPf)[0]*2:
                #     print("bu tree bigger")
                #     print(filename)
                #     print(gen2)
                #     print(min(basisMPf))
                # elif gen2 < min(basisMPf)[0]:
                #     print("Something goes wrong")



                if min([bu[0] for bu in buD]) != min([bu[0] for bu in basisMPf]):
                    print(min([bu[0] for bu in buD]), end=", ")
                    print(min([bu[0] for bu in basisMPf]))
                else:
                    print(filename)


            # for i in gen_bu2(at, at.root, semi):
            #     print(i[0])
            #     for node in i[1]:
            #         print(node.label, end=" ")
            #     print()
            #     print(i[2])




if __name__ == "__main__":
    main()
