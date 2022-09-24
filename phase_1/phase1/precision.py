import decimal

def precision(a,pre):
    if pre == 0 :
        return a
    f = str(a)
    decimal.getcontext().prec = pre
    if (a < pow(10,pre)):
        a = decimal.Decimal(a).__mul__(1)
    else:
        a = int(a)
        f = str(a)
        #print(len(f))
        for i in range(pre,len(f)):
            #print(i)
            f = f[:i] + "0" + f[i + 1:]
        a = float(f)
    return float(a)