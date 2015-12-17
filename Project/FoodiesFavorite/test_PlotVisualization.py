#Authors: Lanyu Shang; Minqing Zhuang; Xing Cui
#GS-DS-1007 Final Project
#Fall 2015
#Instructor: Gregory R Watson

import unittest
from PlotVisualization import *
from LoadData import LoadData
import os


class TestPlotVisualization(unittest.TestCase):
    """
    This class will test functions in PlotVisualization and check if plots are generated successfully.
    """
    @classmethod
    def setUpClass(cls):
        cls.pv = PlotVisualization(LoadData().df)
        cls.pv.user_choice = {'Cuisine_Category': 'EastAsian', 'Cuisine': 'Ramen',
                              'Neighborhood_Category': 'Chelsea and Midtown West', 'Neighborhood': 'Chelsea'}

    def test_init(self):
        self.assertEqual(self.pv.df.shape, (9012, 39))
        self.assertEqual(len(self.pv.xticks_nbhd_names.keys()), 10)
        self.assertEqual(len(self.pv.xticks_feature_names.keys()), 7)

    def test_plot_total_by_nbhd(self):
        try:
            os.remove('total_by_nbhd.jpg')
        except OSError:
            pass
        self.pv.plot_total_by_nbhd()
        self.assertTrue(os.path.isfile('total_by_nbhd.jpg'), "Fail to generate plot.")

    def test_plot_total_by_cuisine(self):
        try:
            os.remove('total_by_cuisine.jpg')
        except OSError:
            pass
        self.pv.plot_total_by_cuisine()
        self.assertTrue(os.path.isfile('total_by_cuisine.jpg'), "Fail to generate plot.")

    def test_plot_num_of_restaurants_in_cuisine_category_given_nbhd_category(self):
        try:
            os.remove('num_of_restaurants_in_cuisines_given_nbhd.jpg')
        except OSError:
            pass
        self.pv.plot_num_of_restaurants_in_cuisine_category_given_nbhd_category()
        self.assertTrue(os.path.isfile('num_of_restaurants_in_cuisines_given_nbhd.jpg'), "Fail to generate plot.")

    def test_plot_num_of_restaurants_in_nbhds_given_cuisine(self):
        try:
            os.remove('num_of_restaurants_in_nbhds_given_cuisine.jpg')
        except OSError:
            pass
        self.pv.plot_num_of_restaurants_in_nbhds_given_cuisine()
        self.assertTrue(os.path.isfile('num_of_restaurants_in_nbhds_given_cuisine.jpg'), "Fail to generate plot.")

    def test_plot_features_of_cuisine_category(self):
        try:
            os.remove('features_of_cuisine.jpg')
        except OSError:
            pass
        self.pv.plot_features_of_cuisine_category()
        self.assertTrue(os.path.isfile('features_of_cuisine.jpg'), "Fail to generate plot.")

    def test_plot_features_of_nbhd_category(self):
        try:
            os.remove('features_of_nbhd.jpg')
        except OSError:
            pass
        self.pv.plot_features_of_nbhd_category()
        self.assertTrue(os.path.isfile('features_of_nbhd.jpg'), "Fail to generate plot.")

    def test_plot_review_of_cuisine_category(self):
        try:
            os.remove('reviews_of_cuisine.jpg')
        except OSError:
            pass
        self.pv.plot_review_of_cuisine_category()
        self.assertTrue(os.path.isfile('reviews_of_cuisine.jpg'), "Fail to generate plot.")

    def test_plot_rating_of_cuisine_category(self):
        try:
            os.remove('ratings_of_cuisine.jpg')
        except OSError:
            pass
        self.pv.plot_rating_of_cuisine_category()
        self.assertTrue(os.path.isfile('ratings_of_cuisine.jpg'), "Fail to generate plot.")



if __name__ == '__main__':
    unittest.main()
