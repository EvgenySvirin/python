import typing
from copy import deepcopy


class Matrix:
    def __init__(self, table):
        self.arr = list(list(row) for row in table)
        self.rows = len(table)
        self.cols = 0 if self.rows == 0 else len(table[1])

    def __add__(self, other: "Matrix"):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"rows: {self.rows}, {other.rows}, cols: {self.cols}, {other.cols}")
        result_arr = deepcopy(self.arr)
        for i in range(self.rows):
            for k in range(self.cols):
                result_arr[i][k] += other.arr[i][k]
        return Matrix(result_arr)

    def __mul__(self, other: "Matrix"):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"rows: {self.rows}, {other.rows}, cols: {self.cols}, {other.cols}")
        result_arr = deepcopy(self.arr)
        for i in range(self.rows):
            for k in range(self.cols):
                result_arr[i][k] *= other.arr[i][k]
        return Matrix(result_arr)

    def __matmul__(self, other: "Matrix"):
        if self.cols != other.rows:
            raise ValueError(f"cols {self.cols} must be equal to rows {other.rows}")

        result_arr = [[0] * other.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for k in range(other.cols):
                for c in range(self.cols):
                    result_arr[i][k] += self.arr[i][c] * other.arr[c][k]
        return Matrix(result_arr)

    def save(self, filename: str):
        with open(filename, 'w') as f:
            for row in self.arr:
                for el in row:
                    f.write(str(el) + ' ')
                f.write('\n')
