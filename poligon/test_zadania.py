from unittest import TestCase
from zadania import Task
import gmpy as gm


class TestTask(TestCase):

    def test_shouldReturnTrueIfNumberIsPrime(self):
        actual = Task.isPrime(3)
        expected = True
        self.assertEqual(expected, actual)

    def test_shouldReturnFalsefNumberIsNotPrime(self):
        actual = Task.isPrime(10)
        expected = False
        self.assertEqual(expected, actual)

    def test_shouldRaiseException(self):
        actual = Task.isPrime(1)
        self.assertEqual(None, actual)

    def test_shouldReturnFirstFibonacciNumber(self):
        actual = Task.getFibonacci(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_shouldReturnSecondFibonacciNumber(self):
        actual = Task.getFibonacci(2)
        expected = 1
        self.assertEqual(expected, actual)

    def test_shouldReturnThirdFibonacciNumber(self):
        actual = Task.getFibonacci(3)
        expected = 2
        self.assertEqual(expected, actual)

    def test_shouldReturnFourthFibonacciNumber(self):
        actual = Task.getFibonacci(4)
        expected = 3
        self.assertEqual(expected, actual)

    def test_shouldReturnNthRoots(self):
        list = [4, 9, 16]
        actual = Task.getNthRoots(list, 2)
        expected = [gm.mpz(2), gm.mpz(3), gm.mpz(4)]
        self.assertEqual(expected, actual)

    def test_shouldCalculateAverage(self):
        list = [10, 20, 30]
        actual = Task.calcualteAverage(list)
        expected = 20
        self.assertEqual(expected, actual)