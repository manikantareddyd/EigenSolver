import numpy as np
from math import copysign
import sys

def InversePower(mat,iterations,threshold):
    try:
        mat = np.linalg.inv(mat)
    except:
        print "Matrix Not Invertible"
        sys.exit(0)
    n = mat.shape[0]
    x = np.array([1 for i in range(n)])
    x.shape = (n,1)
    for i in range(iterations):
        u = mat.dot(x)
        u.shape = (1,n)
        tmpM = max(u.max(),u.min(),key=abs)
        try:
            # print 1, u.max(), M
            err = 100.0*(tmpM-M)/tmpM
            err = copysign(err,1)
            if err<threshold :
                print i+1,"\t\t", u/tmpM,"\t\t", tmpM,"\t\t", err
                print "Error Threshold Hit"
                u.shape = (n,1)
                return tmpM,u/tmpM
            M = tmpM
            x = u/M
            print i+1,"\t\t", x,"\t\t", tmpM,"\t\t", err
        except:
            M = tmpM
            x = u/M
            print i+1,"\t\t", x,"\t\t", M
        x.shape = (n,1)
    
    print "Exceeded total Iterations"
    return M,x

if __name__=="__main__" :
    with open("input.txt") as f:
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    e,v = InversePower(mat,20,0.1)
    v.shape = (1,v.shape[0])
    print "_"*64,"\n"
    print "Eigen Value:\t",e
    print "Eigen Vector:\t",v

