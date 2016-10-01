import QRDecomposition
import numpy as np
import scipy.linalg
import math

def QRMethod(mat,iterations,threshold):
    prevQ, prevR = QRDecomposition.Decompose(mat)
    mat = np.dot(prevR,prevQ)
    for i in range(1,iterations):
        Q, R = QRDecomposition.Decompose(mat)
        mat = np.dot(R,Q)
        error = []
        
        for t in range(Q.shape[0]):
            try:
                e = abs((R[t][t] - prevR[t][t])*100/R[t][t])
                error.append(e)
            except:
                e = 100
                error.append(e)
        print i+1, max(error)
        if max(error) < threshold: 
            print "\nEigenvalues: "
            for t in range(R.shape[0]): print abs(R[t][t])
            print "Number of Iterations: ", i+1
            return
        prevR = R
        prevQ = Q
    
    print "\nEigenvalues: "
    for t in range(R.shape[0]): print abs(R[t][t])
    print "Number of Iterations: ", i+1
    

if __name__=="__main__" :
    with open("input.txt") as f:
        mat = [[float(x) for x in line.split()] for line in f]
    mat = np.matrix(mat)
    QRMethod(mat,10,0.001)
    