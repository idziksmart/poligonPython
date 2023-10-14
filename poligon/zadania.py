import math as m
import gmpy as gm
from statistics import mean


class Task:

    def is_prime(number):
        try:
            if number < 2:
                raise Exception("Number should be greater than 1")
        except:
            return None

        isPrime = True
        for i in range(2, int(m.sqrt(number)), 1):
            if number % i == 0:
                isPrime = False
        return isPrime

    def get_fibonacci(number):
        if (number == 1 or number == 2):
            return 1
        else:
            return Task.get_fibonacci(number - 1) + Task.get_fibonacci(number - 2)

    def get_nth_roots(list, number):
        for i, value in enumerate(list):
            list[i] = gm.root(list[i], number)[0]
        return list

    def calculate_average(list):
        return mean(list)
