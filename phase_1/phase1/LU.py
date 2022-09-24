import time
from copy import deepcopy
from tkinter import messagebox
from phase1 import precision

########################################################################################
n = 0
s = [0.0]
o = [0.0]
y = [0.0]
x = [0.0]
b = []
tol = pow(10, -5)
er = 0

def Pivot(k,a) :
    global  o, s, n, er, x            #Find the largest scaled coefficient in column k
    p = k                               # p is the index to the pivot row
    big = abs((a[o[k]][k]) /float(s[o[k]]))
    for i in range(k + 1, n):
        dummy = abs(a[o[i]][k] / float(s[o[i]]))
        if dummy > big:
            big = dummy
            p = i
            #Swap row k with the pivot row by swapping the
            #indexes. The actual rows remain unchanged
    dummy = o[p]
    o[p] = o[k]
    o[k] = dummy


########################################################################################
#decomposing A into L and U

def Decompose(A,B,n,pre) :
    global o, b, s, er,x, y,tol
    for i in range(n):                  # Find scaling factors
        o[i] = i
        s[i] = abs(A[0][i][0])
        for j in range(1, n) :
            if abs(A[0][i][j]) > s[i]:
                s[i] = abs(A[0][i][j])

    counter = 0
    for k in range(0, n - 1) :
        a = deepcopy(A[counter])
        Pivot(k,a)                        # Locate the kth pivot row

        #Check for singular or near-singular cases
        if (abs(a[o[k]][k]) / float(s[o[k]])) < tol:
            er = -1
            return

        for i in range(k + 1, n):

            factor = a[o[i]][k] / float(a[o[k]][k])
            factor = precision.precision(factor,pre)
            #We reuse the space in A to store the coefficients of L.
            a[o[i]][k] = factor
            #Eliminate the coefficients at column j
            #in the subsequent rows
            for j in range(k + 1, n):
                a[o[i]][j] = a[o[i]][j] - factor * a[o[k]][j]
                a[o[i]][j] = precision.precision(a[o[i]][j],pre)
                #end of "for k" loop from previous page
                #Check for singular or near-singular cases
        A.append(a)
        counter+=1
        B.append(b)
    if (abs(a[o[n - 1]][n - 1]) / float(s[o[n - 1]])) < tol:
        er = -1

########################################################################################
#solving LUx = b

def Substitute(a,pre) :
    global o, b, s, n, er,x, y

    #forward substitution
    y[o[0]] = b[o[0]]
    for i in range(1, n): #i = 2 n = 3
        sum = b[o[i]]
        for j in range(0, i):  #i =  2
            sum = sum - a[o[i]][j] * y[o[j]]
            sum = precision.precision(sum,pre)

        y[o[i]] = sum

    #back substitution
    x[n - 1] = y[o[n - 1]] / float(a[o[n - 1]][n - 1])
    x[n - 1] = precision.precision(x[n - 1],pre)
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range (i + 1, n):
            sum = sum + a[o[i]][j] * x[j]
            sum = precision.precision(sum,pre)

        x[i] = (y[o[i]] - sum) / float(a[o[i]][i])
        x[i] = precision.precision(x[i],pre)

########################################################################################
def LUDecomp(a,b1,noVar,pre):
    global s,o,y,x,n,b
    b = b1
    n = noVar
    s = [0.0] * n
    o = [0.0] * n
    y = [0.0] * n
    x = [0.0] * n
    t1 = time.time()
    A = []
    B = []
    A.append(deepcopy(a))
    B.append(deepcopy(b))
    Decompose(A,B,n,pre)

    if er != -1:
        Substitute(A[len(A)-1],pre)
        print (x)
    else:
        messagebox.showerror("invalid variable", "Has no solution")
    t2 = time.time()
    return (t1,t2,x,A,B)


