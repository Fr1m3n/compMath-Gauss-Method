from components.Vector import Vector
from typing import List


class Matrix:

    def __init__(self):
        self.lines: List[Vector] = []
        self.swaps = 0

    def add_line(self, line):
        self.lines.append(line)

    def swap(self, i, j, b_vector: Vector = None):
        self[i], self[j] = self[j], self[i]
        if b_vector is not None:
            b_vector[i], b_vector[j] = b_vector[j], b_vector[i]
        self.swaps += 1

    def __getitem__(self, item):
        return self.lines[item]

    def __setitem__(self, key, value):
        self.lines[key] = value

    def get_triangle(self, b_vector: Vector):
        n = len(self.lines)
        for i in range(n):
            if self[i][i] == 0:
                if not self._fix_zero(i + 1, i, b_vector):
                    continue
            for k in range(i + 1, n):
                c = self[k][i] / self[i][i]
                self[k][i] = 0
                for j in range(i + 1, n):
                    self[k][j] -= c * self[i][j]
                b_vector[k] -= c * b_vector[i]

    def _fix_zero(self, i, j, b_vector: Vector):
        temp = i
        while i < len(self.lines):
            if self[i][j] != 0:
                self.swap(temp, i, b_vector)
                return True
            i += 1
        return False

    def det(self):
        det = 1
        for i in range(len(self.lines)):
            det *= self[i][i]
        return det * ((-1) ** self.swaps)

    def solve(self, b_vector: Vector):
        n = len(self.lines)
        x_vector = Vector([0 for _ in range(n)])
        for i in range(n - 1, -1, -1):
            s = 0
            for j in range(i + 1, n):
                s += self[i][j] * x_vector[j]
            x_vector[i] = (b_vector[i] - s) / self[i][i]
        return x_vector

    def get_discrepancy(self, x_vector: Vector, b_vector: Vector) -> Vector:
        n = len(self.lines)
        r_vector = Vector([0 for _ in range(n)])
        for i in range(n):
            s = 0
            for j in range(n):
                s += x_vector[j] * self[i][j]
            r_vector[i] = s - b_vector[i]
        return r_vector

    def __str__(self):
        return '\n'.join(map(str, self.lines))
