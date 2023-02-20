from unittest import TestCase
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from numpy.testing import assert_, assert_raises
import exercise
import unittest

class Evaluate(TestCase):
    def test_exercise(self):
        pass

class TestTrainTestSplit(TestCase):
    def test_train_test_split(self):
        iris = exercise.get_iris_dataset()
        X_train, X_test, Y_train, Y_test = exercise.perform_train_test_split()
        self.assertTrue("target" not in X_train.columns)
        self.assertTrue("target" not in X_test.columns)
        self.assertTrue("target" == Y_train.name)
        self.assertTrue("target" == Y_test.name)
        self.assertTrue(X_train.shape[0] + X_test.shape[0] == iris.shape[0])
        self.assertTrue(Y_train.shape[0] + Y_test.shape[0] == iris.shape[0])

class TestNinetyPercentAccuracyModel(TestCase):
    def test_90_percent_accuracy_model(self):
        model, accuracy = exercise.accuracy_at_least_90()
        self.assertTrue(type(model).__name__ == "DecisionTreeClassifier" or type(model).__name__ == "SVC" or type(model).__name__ == "KNeighborsClassifier" or type(model).__name__ == "MLPClassifier")
        self.assertTrue(accuracy >= 0.9)

if __name__ == '__main__':
    unittest.main()