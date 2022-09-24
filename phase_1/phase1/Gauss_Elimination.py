# # importing the module
import time
from tkinter import messagebox
from numpy import *
from copy import copy, deepcopy
import decimal

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
    cpy = deepcopy(Alist)
    for i in range(SIZE):
        factor = max([abs(x) for x in cpy[i]])
        for j in range(SIZE):
            if cpy[i][j] != 0:
                cpy[i][j] /= factor
    row = max_row(cpy, k, SIZE)
    change_Rows(Alist, Blist, k, row)

def Gauss_Elimination(Alist, Blist, SIZE,pre):
    t1 = time.time()
    result = [0]*SIZE
    finalA = []
    finalB = []
    finalA.append(deepcopy(Alist)),finalB.append(Blist)
    decimal.getcontext().prec = 3
    # Forward Elimination:
    for k in range(SIZE-1):
        scaleAndPivot(Alist, Blist, SIZE, k)
        for i in range(k+1, SIZE):
            if Alist[k][k] == 0:
                continue
            factor = Alist[i][k] / Alist[k][k]
            factor = precision.precision(factor,pre)
            for j in range(k, SIZE):
                Alist[i][j] = Alist[i][j] - factor * Alist[k][j]
                Alist[i][j] = precision.precision(Alist[i][j] ,pre)
            Blist[i] = Blist[i] - factor * Blist[k]
            Blist[i] = precision.precision(Blist[i] ,pre)

        finalA.append(deepcopy(Alist))
        finalB.append(deepcopy(Blist))


    # Backward Substitution:
    if Alist[SIZE-1][SIZE-1] == 0:
        print("No unique solution!")
        return (None*3)
    result[SIZE-1] = Blist[SIZE-1] / Alist[SIZE-1][SIZE-1]
    for i in range(SIZE-2, -1, -1):
        if Alist[i][i] == 0:
            print("No unique solution!")
            return (None*3)
        sum = 0
        for j in range(i+1, SIZE):
            sum = sum + Alist[i][j] * result[j]
        result[i] = (Blist[i] - sum) / Alist[i][i]
    t2 = time.time()
    return (t1,t2,result, finalA, finalB)