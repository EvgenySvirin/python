import typing
from copy import deepcopy


class ArrWrapper:
    def __init__(self, value):
        self.arr = value
        self._rows = len(self.arr)
        self._cols = len(self.arr[0]) if 0 < self.rows else 0

    @property
    def arr(self):
        return self._arr

    @arr.setter
    def arr(self, value):
        self._arr = value
        self._rows = len(self.arr)
        self._cols = len(self.arr[0]) if 0 < self.rows else 0

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return self._cols


class HashArrWrapper(ArrWrapper):
    def __init__(self, arr):
        super().__init__(arr)

    def __hash__(self) -> int:
        res = 0
        for row in self.arr:
            for elem in row:
                res += elem % 2
        return res


class Matrix(HashArrWrapper):
    def __init__(self, arr):
        super().__init__(arr)
        self.cache = dict()

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

    def matmul(self, other: "Matrix"):
        if self.cols != other.rows:
            raise ValueError(f"cols {self.cols} must be equal to rows {other.rows}")

        result_arr = [[0] * other.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for k in range(other.cols):
                for c in range(self.cols):
                    result_arr[i][k] += self.arr[i][c] * other.arr[c][k]
        return Matrix(result_arr)

    def __matmul__(self, other: "Matrix"):
        if self.cols != other.rows:
            raise ValueError(f"cols {self.cols} must be equal to rows {other.rows}")

        hashed = other.__hash__()
        if hashed in self.cache:
            return self.cache.get(hashed)
        res = self.matmul(other)
        self.cache[hashed] = res

        return res

    def save(self, filename: str):
        with open(filename, 'w') as f:
            for row in self.arr:
                for el in row:
                    f.write(str(el) + ' ')
                f.write('\n')
