#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson

import unittest
from LoadData import LoadData, Neighborhood, Cuisine


class TestNeighborhood(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        n = Neighborhood()
        self.assertEqual(len(n.nbhd_map.keys()), 10)
        self.assertEqual(len(n.nbhd_category.keys()), 10)


class TestCuisine(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        c = Cuisine()
        self.assertEqual(len(c.cuisine_map.keys()), 11)
        self.assertEqual(len(c.cuisine_category.keys()), 11)


class TestLoadData(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        self.ld = LoadData()
        self.assertEqual(self.ld.df.shape, (9012, 39))

if __name__ == '__main__':
    unittest.main()
