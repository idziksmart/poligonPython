from unittest import TestCase
from zadania import Task
import gmpy as gm


class TestTask(TestCase):

    def test_should_return_true_if_number_is_prime(self):
        actual = Task.is_prime(3)
        expected = True
        self.assertEqual(expected, actual)

    def test_should_return_false_number_is_not_prime(self):
        actual = Task.is_prime(10)
        expected = False
        self.assertEqual(expected, actual)

    def test_should_raise_exception(self):
        actual = Task.is_prime(1)
        self.assertEqual(None, actual)

    def test_should_return_first_fibonacci_number(self):
        actual = Task.get_fibonacci(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_should_return_second_fibonacci_number(self):
        actual = Task.get_fibonacci(2)
        expected = 1
        self.assertEqual(expected, actual)

    def test_should_return_third_fibonacci_number(self):
        actual = Task.get_fibonacci(3)
        expected = 2
        self.assertEqual(expected, actual)

    def test_should_return_fourth_fibonacci_number(self):
        actual = Task.get_fibonacci(4)
        expected = 3
        self.assertEqual(expected, actual)

    def test_should_return_nth_roots(self):
        list = [4, 9, 16]
        actual = Task.get_nth_roots(list, 2)
        expected = [gm.mpz(2), gm.mpz(3), gm.mpz(4)]
        self.assertEqual(expected, actual)

    def test_should_calculate_average(self):
        list = [10, 20, 30]
        actual = Task.calculate_average(list)
        expected = 20
        self.assertEqual(expected, actual)