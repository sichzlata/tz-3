from math import inf
from functools import reduce

class Solution:
    __slots__ = ['input_file']

    def __init__(self, filename):
        self.input_file = filename

    def find_minimum(self):
        res = inf
        with open(self.input_file, 'r') as file:
            for line in file:
                res = min(res, min(map(int, line.rsplit())))
        return res


    def find_maximum(self):
        res = -inf
        with open(self.input_file, 'r') as file:
            for line in file:
                res = max(res, max(map(int, line.rsplit())))
        return res

    def sum(self):
        res = 0
        with open(self.input_file, 'r') as file:
            for line in file:
                res += sum(map(int, line.rsplit()))
        return res

    def product(self):
        res = 1
        with open(self.input_file, 'r') as file:
            for line in file:
                res *= reduce(lambda x, y: x * y, (map(int, line.rsplit())))
        return res

print("Назовите файл с данными input.txt")
s1 = Solution("input.txt")
print("Минимум:", s1.find_minimum())
print("Максимум:", s1.find_maximum())
print("Сумма:", s1.sum())
print("Произведение:", s1.product())
