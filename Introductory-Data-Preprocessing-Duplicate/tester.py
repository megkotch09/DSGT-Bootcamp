from unittest import TestCase

from numpy.testing import assert_, assert_raises
import unittest
import exercise
import pandas as pd

class Evaluate(TestCase):
    def test_exercise(self):
        pass

class TestGetFeatureNames(TestCase):
    def test_proper_feature_titles(self):
        expected = ["alcohol",	"malic_acid",	"ash",	"alcalinity_of_ash",	"magnesium",	"total_phenols",	"flavanoids",	"nonflavanoid_phenols",	"proanthocyanins",	"color_intensity",	"hue",	"od280/od315_of_diluted_wines",	"proline"]
        self.assertTrue(list(exercise.get_feature_titles()) == expected)
        self.assertTrue(len(expected) == len(list(exercise.get_feature_titles())))

class TestAddTwo(TestCase):
    def test_added_two_to_magnesium(self):
        original = exercise.get_wine_data()
        result = exercise.add_2_to_magnesium()
        diff = [a-b for a,b in zip(list(result["magnesium"]), list(original["magnesium"]))]
        self.assertTrue(set(diff) == set([2.0]))

class TestFlavToNonFlav(TestCase):
    def test_flav_to_non_flav_ratio(self):
        expected = [10.928571428571427, 10.615384615384615, 10.8, 14.541666666666668, 6.897435897435897]
        self.assertTrue(list(exercise.create_flav_to_non_flav_ratio()["flav_to_non_flav"]) == expected)

class TestAlcoholSifter(TestCase):
    def test_alcohol_content_level_sifter(self):
        result = exercise.alcohol_content_level_sifter()
        alcohol_counts = dict(result["alcohol"].value_counts())
        content_level_counts = dict(result["alcohol_content_level"].value_counts())
        count_high = 0
        count_low = 0
        for k in alcohol_counts.keys():
            if (k > 13.5):
                count_high += alcohol_counts[k]
            else:
                count_low += alcohol_counts[k]
        self.assertTrue(content_level_counts[0] == count_low)
        self.assertTrue(content_level_counts[1] == count_high)

class TestGetNumMissingValues(TestCase):
    def test_missing_vals(self):
        missing_vals = dict(exercise.get_num_missing_values())
        for k in missing_vals:
            self.assertTrue(missing_vals[k] == 0)

if __name__ == '__main__':
    unittest.main()