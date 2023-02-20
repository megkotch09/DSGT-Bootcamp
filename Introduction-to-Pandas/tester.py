from unittest import TestCase

from numpy.testing import assert_, assert_raises

import unittest
import pandas as pd

import exercise

class Evaluate(TestCase):
    def test_exercise(self):
        pass

class TestProperAgeClassSex(TestCase):
    def test_proper_age_class_sex(self):
        titanic = exercise.get_dataframe()
        res = exercise.get_age_class_sex()
        self.assertEqual(list(res.columns), ["Age", "Pclass", "Sex"])
        self.assertEqual(res.shape[0], titanic.shape[0])

class TestAgeClassSexOverThirty(TestCase):
    def test_proper_entries_over_30(self):
        titanic = exercise.get_dataframe()
        res = exercise.get_age_class_sex_over_30()
        cols = list(res.columns)
        self.assertEqual(len(cols), len(["Age", "Pclass", "Sex"]))
        self.assertTrue("Age" in cols)
        self.assertTrue("Pclass" in cols)
        self.assertTrue("Sex" in cols)
        self.assertTrue(res["Age"].min() > 30)
        self.assertTrue(res.shape[0] <= titanic.shape[0])

class TestHundredthPerson(TestCase):
    def test_100th_row_info(self):
        titanic = exercise.get_dataframe()
        res = exercise.get_100th_person_info()
        self.assertTrue(res["PassengerId"] == 100)
        self.assertTrue(res["Survived"] == 0)
        self.assertTrue(res["Pclass"] == 2)
        self.assertTrue(res["Name"] == "Kantor, Mr. Sinai")
        self.assertTrue(res["Sex"] == "male")
        self.assertTrue(res["Age"] == 34)
        self.assertTrue(res["SibSp"] == 1)
        self.assertTrue(res["Parch"] == 0)
        self.assertTrue(res["Ticket"] == "244367")
        self.assertTrue(res["Fare"] == 26)
        self.assertTrue(res["Embarked"] == "S")

class TestNumUniqueAges(TestCase):
    def test_num_unique_ages(self):
        res = exercise.calc_num_unique_ages()
        self.assertTrue(res == 88)

class TestCabinNullsAndShape(TestCase):
    def test_cabin_null_count_and_shape(self):
        self.assertTrue(exercise.get_cabin_nulls_and_shape()[0] == 687)
        self.assertTrue(exercise.get_cabin_nulls_and_shape()[1] == 891)

class TestDropCabinCol(TestCase):
    def test_drop_cabin_col(self):
        titanic = exercise.get_dataframe()
        filtered = exercise.drop_cabin_col()
        assert "Cabin" not in list(filtered.columns)
        assert len(list(filtered.columns)) == len(list(titanic.columns)) - 1
        assert filtered.shape[0] == titanic.shape[0]

class TestSurvivedWithinEachClass(TestCase):
    def test_survived_within_each_class(self):
        result = exercise.survived_within_class()
        self.assertEqual(result[0], 0.630)
        self.assertEqual(result[1], 0.473)
        self.assertEqual(result[2], 0.242)

if __name__ == '__main__':
    unittest.main()