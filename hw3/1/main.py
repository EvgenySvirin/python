import numpy as np
from matrix import Matrix

if __name__ == '__main__':
    np.random.seed(0)
    A = Matrix(np.random.randint(0, 10, (10, 10)))
    B = Matrix(np.random.randint(0, 10, (10, 10)))

    (A + B).save("artifacts/matrix+.txt")
    (A * B).save("artifacts/matrix*.txt")
    (A @ B).save("artifacts/matrix@.txt")

    res1 = np.array((A + B).arr)
    res2 = np.array(np.array(A.arr) + np.array(B.arr))
    assert np.all(res1 == res2)

    res3 = np.array((A * B).arr)
    res4 = np.array(np.array(A.arr) * np.array(B.arr))
    assert np.all(res3 == res4)

    res5 = np.array((A @ B).arr)
    res6 = np.array(np.matmul(np.array(A.arr), np.array(B.arr)))
    assert np.all(res5 == res6)

