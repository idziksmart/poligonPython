import math as m
import gmpy as gm
from statistics import mean


class Task:

    def isPrime(number):
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

    def getFibonacci(number):
        if (number == 1 or number == 2):
            return 1
        else:
            return Task.getFibonacci(number - 1) + Task.getFibonacci(number - 2)

    def getNthRoots(list, number):
        for i, value in enumerate(list):
            list[i] = gm.root(list[i], number)[0]
        return list

    def calcualteAverage(list):
        return mean(list)
