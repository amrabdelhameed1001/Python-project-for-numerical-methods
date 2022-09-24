import copy
import time
from phase1 import precision


def change_Rows(Alist, Blist, r1, r2):
    if r1 != r2:
        Alist[r1], Alist[r2] = Alist[r2], Alist[r1]
        Blist[r1], Blist[r2] = Blist[r2], Blist[r1]

def max_row(Alist, c, SIZE):
    """ returns the index of row that has max element in column c of Alist from start or after"""
    # start  = c
    MAX_VALUE = abs(Alist[c][c])
    MAX_INDEX = c
    for i in range(c+1, SIZE):
        if abs(Alist[i][c]) > MAX_VALUE:
            MAX_VALUE = abs(Alist[i][c])
            MAX_INDEX = i
    return MAX_INDEX

def scaleAndPivot(Alist, Blist, SIZE, k):
    cpy = copy.deepcopy(Alist)
    for i in range(SIZE):
        factor = max([abs(x) for x in cpy[i]])
        for j in range(SIZE):
            if cpy[i][j] != 0:
                cpy[i][j] /= factor
    row = max_row(cpy, k, SIZE)
    change_Rows(Alist, Blist, k, row)

def Gauss_Jordan(Alist, Blist, SIZE,pre):
    t1 = time.time()
    result = [0]*SIZE
    finalA = []
    finalB = []

    # Bi-Direction Elimination:
    for k in range(SIZE):
        scaleAndPivot(Alist, Blist, SIZE, k)
        if Alist[k][k] == 0:
            continue
        factor = Alist[k][k]
        factor = precision.precision(factor,pre)
        for m in range(SIZE):
            Alist[k][m] = Alist[k][m] / factor
            Alist[k][m] = precision.precision( Alist[k][m],pre)
        Blist[k] = Blist[k] / factor
        Blist[k] = precision.precision(Blist[k],pre)

        for i in range(k+1, SIZE):
            factor = Alist[i][k] / Alist[k][k]
            factor = precision.precision(factor,pre)
            for j in range(k, SIZE):
                Alist[i][j] = Alist[i][j] - factor * Alist[k][j]
                Alist[i][j] = precision.precision(Alist[i][j],pre)
            Blist[i] = Blist[i] - factor * Blist[k]
            Blist[i] = precision.precision(Blist[i],pre)

        for l in range(k-1, -1, -1):
            factor = Alist[l][k] / Alist[k][k]
            factor = precision.precision(factor,pre)
            for j in range(0, SIZE):
                Alist[l][j] = Alist[l][j] - factor * Alist[k][j]
                Alist[l][j] = precision.precision(Alist[l][j],pre)
            Blist[l] = Blist[l] - factor * Blist[k]
            Blist[l] = precision.precision(Blist[l],pre)

        finalA.append(copy.deepcopy(Alist))
        finalB.append(copy.deepcopy(Blist))
    t2=time.time()
    return (t1,t2,Blist, finalA, finalB)