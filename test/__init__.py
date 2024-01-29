import unittest

from src.example_tree.generate import main
from src.model.ring.semi_ring import MiniumCostMetricTree
from src.algorithm.bu_basis import BuBasis
from src.algorithm.bu_basisMP import BuBasisMP
from src.algorithm.bu_basisMPfilter import BuBasisMPfilter
from src.model.ring.semi_ring import MiniumCostMetricTree
from src.reader.reader import *
from src.algorithm.bu_tree import *
import os



class TestDifferenInstance(unittest.TestCase):
    def setUp(self):
        # generate
        # main(100, 100, 10, 100)
        # self.path = "..\src\example_tree\generate\generate10010010100"
        self.path = "..\src\example_tree"
        self.semi = MiniumCostMetricTree("int")
        self.bottom_up_tree = BottomUpTree()
        self.bottom_up = BuBasis()
        self.bottom_up_mp = BuBasisMP()
        self.bu_Bmp_filter = BuBasisMPfilter()
    def test_bu(self):
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".at"):
                at = get_list_of_at(self.path + "\\" + filename)[0]
                with open((self.path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                    write_dot(at, f)
                self.assertTrue(self.bottom_up_tree.run(at, at.root, self.semi) >0, "Not bigger then zero, not dynamic")
                self.assertTrue(self.bottom_up_tree.run_dp(at, at.root, self.semi) > 0, "Not bigger then zero, dynamic")
    def test_buBAS(self):
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".at"):
                at = get_list_of_at(self.path + "\\" + filename)[0]
                with open((self.path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                    write_dot(at, f)
                a0 = self.bottom_up.run(at, at.root, self.semi)
                a1 = self.bottom_up.run_dp(at, at.root, self.semi)
                self.assertTrue(min(a0)[0]> 0,
                                "Not bigger then zero, not dynamic")
                self.assertTrue(min(a1)[0] > 0, "Not bigger then zero, dynamic")
                self.assertEquals(a0,a1)

    def test_buMP(self):
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".at"):
                at = get_list_of_at(self.path + "\\" + filename)[0]
                with open((self.path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                    write_dot(at, f)
                a0 = self.bottom_up_mp.run(at, at.root, self.semi)
                a1 = self.bottom_up_mp.run_dp(at, at.root, self.semi)
                self.assertTrue(min(a0)[0] > 0,
                                "Not bigger then zero, not dynamic")
                self.assertTrue(min(a1)[0] > 0, "Not bigger then zero, dynamic")
                self.assertEquals(a0, a1)

    def test_buMPfilter(self):
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".at"):
                at = get_list_of_at(self.path + "\\" + filename)[0]
                with open((self.path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                    write_dot(at, f)
                a0 = self.bu_Bmp_filter.run(at, at.root, self.semi)
                a1 = self.bu_Bmp_filter.run_dp(at, at.root, self.semi)
                self.assertTrue(min(a0)[0] > 0,
                                "Not bigger then zero, not dynamic")
                self.assertTrue(min(a1)[0] > 0, "Not bigger then zero, dynamic")
                self.assertEquals(a0, a1)

    def test_buCompair(self):
        for file in os.listdir(self.path):
            filename = os.fsdecode(file)
            if filename.endswith(".at"):
                at = get_list_of_at(self.path + "\\" + filename)[0]
                with open((self.path + "\\" + filename).replace(".at", ".dot"), 'w') as f:
                    write_dot(at, f)
                a0 = self.bu_Bmp_filter.run(at, at.root, self.semi)
                a1 = self.bu_Bmp_filter.run_dp(at, at.root, self.semi)
                self.assertTrue(min(a0)[0] > 0,
                                "Not bigger then zero, not dynamic")
                self.assertTrue(min(a1)[0] > 0, "Not bigger then zero, dynamic")
                self.assertEquals(a0, a1)


if __name__ == '__main__':
    unittest.main()