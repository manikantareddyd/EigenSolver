import numpy as np

def DirectPower(mat,iterations):
    n = mat.shape[0]
    x = np.array([1 for i in range(n)])
    x.shape = (3,1)
    for i in range(iterations):
        u = mat.dot(x)
        M = u.max()
        x = u/M
    return M
if __name__=="__main__" :
    with open("input.txt") as f:
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    poo = DirectPower(mat,20)
    print poo


