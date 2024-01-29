from src.algorithm.bu_basis import BuBasis
from src.algorithm.bu_basisMP import BuBasisMP
from src.algorithm.bu_basisMPfilter import BuBasisMPfilter
from src.model.ring.semi_ring import MiniumCostMetricTree
from src.reader.reader import *
from src.algorithm.bu_tree import *
import os


def main():
    path = "..\src\example_tree"
    semi = MiniumCostMetricTree("int")
    bottom_up_tree = BottomUpTree()
    bottom_up = BuBasis()
    bottom_up_mp = BuBasisMP()
    bu_Bmp_filter = BuBasisMPfilter()

    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if filename.endswith(".at"):
            at = get_list_of_at(path + "\\" + filename)[0]
            with open((path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                write_dot(at, f)
            # gen_bu(at,at.root, semi)
            # print(min([bu[0] for bu in gen_bu(at, at.root, semi)]), end=", ")
            # gen_bu2(at,at.root, semi)
            # print(min([bu[0] for bu in gen_bu2(at, at.root, semi)]))
            if (not (filename.__contains__("100"))):
                # if True:
                basis = bottom_up.run(at, at.root, semi)
                basis_lp = bottom_up.run_dp(at, at.root, semi)

                if min([bu[0] for bu in basis]) != min([bu[0] for bu in basis_lp]):
                    print(min([bu[0] for bu in basis]), end=", ")
                    print(min([bu[0] for bu in basis_lp]))
                else:
                    print(filename)
                    print(min([bu[0] for bu in basis]))

            # for i in gen_bu2(at, at.root, semi):
            #     print(i[0])
            #     for node in i[1]:
            #         print(node.label, end=" ")
            #     print()
            #     print(i[2])


if __name__ == "__main__":
    main()
