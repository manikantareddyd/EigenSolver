import numpy as np
from math import copysign

def DirectPower(mat,iterations,threshold):
    n = mat.shape[0]
    x = np.array([1 for i in range(n)])
    x.shape = (3,1)
    for i in range(iterations):
        u = mat.dot(x)
        try:
            # print 1, u.max(), M
            err = 100.0*(u.max()-M)/u.max()
            err = copysign(err,1)
            if err<threshold :
                return u.max()
            print i+1, u/u.max(), u.max(), err
            
            M = u.max()
            x = u/M
        except:
            M = u.max()
            x = u/M
            print i+1, x, M
    return M
if __name__=="__main__" :
    with open("input.txt") as f:
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    poo = DirectPower(mat,20,0.1)
    print poo


