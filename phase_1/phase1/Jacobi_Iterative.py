import time
from phase1 import precision

def Jacobi_Iterative(Alist, Blist, SIZE, guess, es, noIterations,pre):
    t1 = time.time()
    result = guess.copy()
    temp = [0]*SIZE
    error = [100]*SIZE
    counter = 0

    final = []

    # print("result:", result, "temp:", temp, "error:", error, "counter:", counter)
    while counter < noIterations and max(error) >= es:
        for i in range(SIZE):
            temp[i] = (Blist[i] - (sum([Alist[i][j]*result[j] for j in range(SIZE)]) - precision.precision( Alist[i][i]*result[i])) / Alist[i][i],pre)
            temp[i] = precision.precision(temp[i],pre)
            error[i] = precision.precision(abs((temp[i] - result[i]) / temp[i]),pre) * 100
            # print("i:", i, "temp[i]:", temp[i], "error[i]:", error[i])
        result = temp.copy()
        # print("result:", result)
        counter += 1

        final.append([result.copy(), error.copy()])
        # print("counter:", counter)
    # print("error:", error, "result:", result)
    t2 = time.time()
    return (t1,t2,error, result, final)