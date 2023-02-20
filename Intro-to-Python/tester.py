from unittest import TestCase
import unittest
import exercise
class Evaluate(TestCase):
    def test_exercise(self):
        pass
class TestCube(TestCase):
    def test_cube_integer(self):
        self.assertEqual(exercise.cube(2), 8)
        self.assertEqual(exercise.cube(5), 125)
        self.assertEqual(exercise.cube(9), 729)
    def test_cube_zero(self):
        self.assertEqual(exercise.cube(0), 0)
    def test_cube_negative_integer(self):
        self.assertEqual(exercise.cube(-1), -1)
        self.assertEqual(exercise.cube(-10), -1000)
        self.assertEqual(exercise.cube(-7), -343)
        self.assertEqual(exercise.cube(-3), -27)
    def test_cube_floating_point_numbers(self):
        self.assertAlmostEqual(exercise.cube(1.1), 1.331)
        self.assertAlmostEqual(exercise.cube(0.9), 0.729)
        self.assertAlmostEqual(exercise.cube(-0.06), -0.000216)
        self.assertAlmostEqual(exercise.cube(5.65), 180.362125)
class TestFactorial(TestCase):
    def test_factorial_normal(self):
        self.assertEqual(exercise.factorial(2), 2)
        self.assertEqual(exercise.factorial(3), 6)
        self.assertEqual(exercise.factorial(5), 120)
    def test_zero_factorial(self):
        self.assertEqual(exercise.factorial(0), 1)
    def factorial_negative_integer(self):
        with self.assertRaises(ValueError):
            exercise.factorial(-1)
            exercise.factorial(-200)
            exercise.factorial(-150)
            exercise.factorial(-7)
    def test_factorial_floating_point_numbers(self):
        with self.assertRaises(ValueError):
            exercise.factorial(1.2)
            exercise.factorial(200.345345)
            exercise.factorial(150.12123)
            exercise.factorial(-7.9)
class TestCountDigits(TestCase):
    def test_count_digits(self):
        self.assertEqual(exercise.count_digits(2), 1)
        self.assertEqual(exercise.count_digits(3), 1)
        self.assertEqual(exercise.count_digits(5), 1)
        self.assertEqual(exercise.count_digits(29), 2)
        self.assertEqual(exercise.count_digits(99), 2)
        self.assertEqual(exercise.count_digits(101), 3)
        self.assertEqual(exercise.count_digits(5045), 4)
        self.assertEqual(exercise.count_digits(0), 1)
        self.assertEqual(exercise.count_digits(123234234), 9)
class TestAverageGrade(TestCase):
    def test_avg_grade_normal(self):
        self.assertEqual(exercise.average_grade({"Exam 1": 43, "Exam 2": 59, "Exam 3": 60, "Exam 4": 90}, 70), 98)
        self.assertEqual(exercise.average_grade({"E1": 90, "E2": 95}, 97), 106)
        self.assertEqual(exercise.average_grade({"E1": 88, "E2": 90, "E3": 94}, 91), 92)
    def test_zeros_on_exams(self):
        self.assertEqual(exercise.average_grade({"E1": 0, "E2": 0, "E3": 0, "E4": 0}, 100), 500)
        self.assertEqual(exercise.average_grade({"E1": 0}, 0), 0)
        self.assertEqual(exercise.average_grade({"E1": 0, "E2": 0}, 30), 90)
    def test_exam_acer(self):
        self.assertEqual(exercise.average_grade({"E1": 100, "E2": 100, "E3": 100, "E4": 100}, 100), 100)
        self.assertEqual(exercise.average_grade({"E1": 100, "E2": 100}, 90), 70)
class TestSliceProduct(TestCase):
    def test_slice_product_normal(self):
        self.assertEqual(exercise.slice_product([1,2,3,4,5], 1, 3), 24)
        self.assertEqual(exercise.slice_product([2,6,7,8,9,3,0,1,4,132,23], 0, 5), 18144)
        self.assertEqual(exercise.slice_product([7,6,14,10,11,9,12,8,15,5,13], 2,8), 19958400)
    def test_slice_product_empty(self):
        with self.assertRaises(ValueError):
            exercise.slice_product([], 0,1)
    def test_slice_product_invalid_start_pos(self):
        with self.assertRaises(ValueError):
            exercise.slice_product([1,23423,3736465,2412342,65868,234123,957,7856,856,78,67,856,785,67,856,78,34,52,3434,23,412,3,214], -9,1)
            exercise.slice_product([235,23,646,456,74,787,86,97,89,5476,34,24,1215,45,6,48,5,689,678,956,4,345,325,66,4,7868,79,979,87,654], -8,1)
            exercise.slice_product([124,1.2,34.12,34.234,52.34,5.234,34.5,2.34,52,3452,34,523,46,34,5654,6,47,67,764,57,54,6,74,56,754], -1,1)
            exercise.slice_product([134,6456,123,0,7,45,3,1,3,4,6,7,8,9,0,6,32,2,4,46], -2,1)
    def test_slice_product_invalid_end_pos(self):
        with self.assertRaises(ValueError):
            exercise.slice_product([1,23423,3736465,2412342,65868,234123,957,7856,856,78,67,856,785,67,856,78,34,52,3434,23,412,3,214], 1,12341234123)
            exercise.slice_product([235,23,646,456,74,787,86,97,89,5476,34,24,1215,45,6,48,5,689,678,956,4,345,325,66,4,7868,79,979,87,654], 5,3555)
            exercise.slice_product([124,1.2,34.12,34.234,52.34,5.234,34.5,2.34,52,3452,34,523,46,34,5654,6,47,67,764,57,54,6,74,56,754], 2,5000)
            exercise.slice_product([134,6456,123,0,7,45,3,1,3,4,6,7,8,9,0,6,32,2,4,46], -2,20)
    def test_slice_product_hidden_zero(self):
        self.assertEqual(exercise.slice_product([1,2,3,0,4,5], 1, 3), 0)
        self.assertEqual(exercise.slice_product([124,1.2,34.12,34.234,0, 52.34,5.234,0, 34.5,2.34,52,3452,34,523,46,34,5654,6,47,67,764,57,54,6,74,56,754], 3,6), 0)
        self.assertEqual(exercise.slice_product([7,6,14,10,11,9,12,8,15,5,0,13], 2,8), 19958400)
class TestEncryption(TestCase):
    def test_encryption_normal(self):
        self.assertEqual(exercise.encrypt("Julius Caesar", 3).lower(), "Mxolxv Fdhvdu".lower())
        self.assertEqual(exercise.encrypt("Hello Data Science", 7).lower(), "Olssv Khah Zjplujl".lower())
        self.assertEqual(exercise.encrypt("Can Bob get me a soda", 30).lower(), "Ger Fsf kix qi e wshe".lower())
    def test_encrypt_empty(self):
        self.assertEqual(exercise.encrypt("", 123).lower(), "".lower())
        self.assertEqual(exercise.encrypt("", 5).lower(), "".lower())
        self.assertEqual(exercise.encrypt("", 4).lower(), "".lower())
    def test_encryption_no_shift(self):
        self.assertEqual(exercise.encrypt("Julius Caesar", 0).lower(), "Julius Caesar".lower())
        self.assertEqual(exercise.encrypt("Hello Data Science", 0).lower(), "Hello Data Science".lower())
        self.assertEqual(exercise.encrypt("Can Bob get me a soda", 0).lower(), "Can Bob get me a soda".lower())
        self.assertEqual(exercise.encrypt("asdfkjasldfjalrkgjoeirghslkdfgjlkadjflkamjf", 0).lower(), "asdfkjasldfjalrkgjoeirghslkdfgjlkadjflkamjf".lower())
    def test_encryption_negative_shift(self):
        self.assertEqual(exercise.encrypt("It is the bottom of the ninth", -27).lower(), "Hs hr sgd anssnl ne sgd mhmsg".lower())
        self.assertEqual(exercise.encrypt("Data science is cool", -300).lower(), "Pmfm eouqzoq ue oaax".lower())
        self.assertEqual(exercise.encrypt("Summertime fun", -2).lower(), "Qskkcprgkc dsl".lower())
class TestDecryption(TestCase):
    def test_decryption_normal(self):
        self.assertEqual(exercise.decrypt("Mxolxv Fdhvdu", 3).lower(), "Julius Caesar".lower())
        self.assertEqual(exercise.decrypt("Olssv Khah Zjplujl", 7).lower(), "Hello Data Science".lower())
        self.assertEqual(exercise.decrypt("Ger Fsf kix qi e wshe", 30).lower(), "Can Bob get me a soda".lower())
    def test_decrypt_empty(self):
        self.assertEqual(exercise.decrypt("", 123).lower(), "".lower())
        self.assertEqual(exercise.decrypt("", 5).lower(), "".lower())
        self.assertEqual(exercise.decrypt("", 4).lower(), "".lower())
    def test_decryption_no_shift(self):
        self.assertEqual(exercise.decrypt("asdfasdfasdfadsf", 0).lower(), "asdfasdfasdfadsf".lower())
        self.assertEqual(exercise.decrypt("HelsdfgsdfgsdfgsdlodsfgsdfgsdhdScfhjtyjtyjhfjdfience", 0).lower(), "HelsdfgsdfgsdfgsdlodsfgsdfgsdhdScfhjtyjtyjhfjdfience".lower())
        self.assertEqual(exercise.decrypt("CawthrtnmtukyunBosdgsdfgbgdfghdfghetsdgfsdfgsdfgmeasdfgsdfgsodsdfgsdfga", 0).lower(), "CawthrtnmtukyunBosdgsdfgbgdfghdfghetsdgfsdfgsdfgmeasdfgsdfgsodsdfgsdfga".lower())
        self.assertEqual(exercise.decrypt("asdfasdfasdfasdfasdfasdfsdfasdf", 0).lower(), "asdfasdfasdfasdfasdfasdfsdfasdf".lower())
    def test_decryption_negative_shift(self):
        self.assertEqual(exercise.decrypt("Hs hr sgd anssnl ne sgd mhmsg", -27).lower(), "It is the bottom of the ninth".lower())
        self.assertEqual(exercise.decrypt("Pmfm eouqzoq ue oaax", -300).lower(), "Data science is cool".lower())
        self.assertEqual(exercise.decrypt("Qskkcprgkc dsl", -2).lower(), "Summertime fun".lower())

if __name__ == '__main__':
    unittest.main()