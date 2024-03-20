import numpy as np


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


class SerializableInArrWrapper(ArrWrapper):
    def save(self, filename):
        with open(filename, "w") as f:
            for row in self.arr:
                for v in row:
                    f.write(str(v))
                    f.write(" ")
                f.write("\n")


class ShowableArrWrapper(ArrWrapper):
    def __str__(self):
        res = ""
        for row in self.arr:
            for v in row:
                res += str(v) + " "
            res += "\n"
        return res


class MixinMatrix(
    np.lib.mixins.NDArrayOperatorsMixin, SerializableInArrWrapper, ShowableArrWrapper
):
    def __init__(self, arr):
        super().__init__(arr)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        inputs = tuple(x.arr if isinstance(x, MixinMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.arr if isinstance(x, MixinMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.arr)
