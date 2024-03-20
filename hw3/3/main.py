import numpy as np
from matrix import Matrix

if __name__ == '__main__':
    np.random.seed(0)
    A = Matrix([[1, 0], [0, 1]])
    B = Matrix([[1, 0], [0, 1]])
    C = Matrix([[3, 0], [0, 1]])
    D = Matrix([[1, 0], [0, 1]])

    AB = A@B
    CD = C@D

    AB.save("artifacts/AB.txt")
    CD.save("artifacts/CD.txt")
    with open("artifacts/hash.txt", 'w') as f:
        f.write(f"AB hash: {str(AB.__hash__())} \n")
        f.write(f"CD hash: {str(CD.__hash__())} \n")



