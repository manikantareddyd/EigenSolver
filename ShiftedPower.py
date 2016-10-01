import numpy as np
from math import copysign

def DirectPower(mat,iterations,threshold):
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

with open("input.txt") as f:
    n = [int(x) for x in next(f).split()][0]
    mat = []
    for i in range(n):
        mat.append([float(x) for x in next(f).split()])
    
    maxIter = [int(x) for x in next(f).split()][0]
    
    maxThres = [float(x) for x in next(f).split()][0]

    shift = [float(x) for x in next(f).split()][0]
    
mat = np.matrix(mat)
identity = np.identity(mat.shape[0])
scalar = 0
print mat
mat = mat - scalar*identity
print mat
# mat = np.linalg.inv(mat)
e,v = DirectPower(mat,100,0.001)
v.shape = (1,v.shape[0])
print "_"*64,"\n"
print "Eigen Value:\t",e+scalar
print "Eigen Vector:\t",v

