from tkinter import *
from tkinter import messagebox
from phase1 import Gauss_Elimination, Gauss_Jordan, LU, Gauss_Seidel, Jacobi_Iterative

root = Tk()
root.title("Numeric Project")
root.geometry("200x300")
# lable widget
title = Label(root, text="Numeric Project\n\n\n\n")
no_var_lab = Label(root, text="number of variable")
no_var = Scale(root, from_=2, to=100, orient=HORIZONTAL)
equation_lab = Label(root)
precision_lab = Label(root, text="precision")
precision = Scale(root, from_=0, to=20, orient=HORIZONTAL)
precision.set(0)
clicked = StringVar()
clicked.set("Gauss Elimination")
list = ['Gauss Elimination', 'Gauss Jordan', 'LU Decomposition', 'Gauss Seidel', 'Jacobi Iteration']
drop = OptionMenu(root, clicked, *list)
# equation_lab.grid()
equation = Entry(root)
i = 1
X_c = 0
A_c = 0
noVar = 0
count = 0
steps = []
res = []
B = []
start = 0
stop = 0


def invalid_variable():
    messagebox.showerror("invalid variable", "invalid variable Name")


def invalid_value():
    messagebox.showerror("invalid value", "No multiplication allowed")


def valid(str):
    global X_c, i, A_c
    tempX = X_c
    tempA = A_c
    # print(str)
    count = -1
    temp = ""
    value = 0.0
    arr = [0.0] * noVar
    if not '=' in str:
        messagebox.showerror("invalid", "equal!!")
        return False
    while (count < len(str) and len(str) != 0):
        count += 1
        # print(cont)
        # print(len(str))
        if (str[count] == 'x'):
            temp = str[0:count:]
            str = str[count + 1::]
            # print(count)
            if (len(temp) == 0):
                value = 1.0
            elif (temp == '-'):
                value = -1.0
            else:
                try:
                    value = float(temp)
                except:
                    invalid_value()
                    return False
            count = -1
            for ch in str:
                count += 1
                if (ch == '+' or ch == '-' or ch == '='):
                    temp = str[0:count:]
                    str = str[count + 1::]
                    if (ch == '-'):
                        str = '-' + str
                    if (ch == '='):
                        try:
                            X[tempX] = float(str)
                            tempX += 1
                            str = ""
                        except:
                            messagebox.showerror("invalid", "equal!!")
                            return False
                    break
            # temp = str[0:i-1:]
            # print(str)
            count = -1
            try:
                # print("here")
                if (int(temp) > noVar or int(temp) < 1):
                    invalid_variable()
                    return False
                    # print("here")
                else:
                    # print(value)
                    arr[int(temp) - 1] += value
            except:
                invalid_variable()
                return False

    A[tempA] = arr
    tempA += 1
    X_c = tempX
    A_c = tempA
    return True


counter = 1
l9 = Label()


def print_res(top, step,f):
    global counter, Back, forward, num
    element = ""
    n = len(steps)
    if f :
        n /= 2
        n = int(n)
    num.grid_forget()
    Back.grid_forget()
    forward.grid_forget()
    if (step == 1):
        counter += 1
    elif (step == 0):
        counter -= 1
    if (counter != 1):
        Back.grid(row=3, column=0)
    if (counter != n):
        forward.grid(row=3, column=2)
    num = Label(top, text=str(counter) + " of " + str(n))
    num.grid(row=2, column=1)
    global l9
    l9.destroy()
    element = ''
    if f :
        element += "res = " + str(steps[(counter - 1)][0]) + "\nerror = " + str(steps[(counter - 1)][1]) + '\n'
    else :
        for j in range(len(steps[counter - 1])):
            element = element + str(steps[counter - 1][j]) + "  " + str(B[counter - 1][j]) + '\n'
    l9 = Label(top, text=element)
    l9.grid(row=1, column=1)


Back = Button()
forward = Button()
num = Label()
itrat = False


def itrative(eps, guess, top, no_iteration):
    global itrat, noItreation, ep, arr
    noItreation = no_iteration.get()
    if (eps.get() == ""):
        eps.insert("1")
    try:
        ep = float(eps.get())
    except:
        temp = False
        messagebox.showerror("invalid", "eps should be number")
        top.destroy()
        solve()
        return
    try:
        v = guess.get().split()
        print(v)
        if (len(v) == noVar):
            print("why")
            for i in range(noVar):
                arr.append(float(v[i]))
        else:
            top.destroy()
            messagebox.showerror("invalid", "guess not equal number of variable")
            solve()
            return
    except:
        if (guess.get() == ""):
            arr = [0.0] * noVar
            top.destroy()
            itrat = True
            solve()
            return
        messagebox.showerror("invalid", "guess should be number")
    top.destroy()
    itrat = len(arr) == noVar
    solve()


ep = 0.0
arr = []
c = 0
noItreation = 0

def dest(top):
    top.destroy()

def solve():
    global A, X, res, steps, B, Back, forward, ep, arr, itrat, c, submit
    # print(A)
    # print(X)
    eps = Entry()
    top = Toplevel()
    start = 0
    stop = 0
    f = False
    no_iteration = Scale()
    if (clicked.get() == list[0]):
        start, stop, res, steps, B = Gauss_Elimination.Gauss_Elimination(A, X, noVar,precision.get())  # ,precision.get()
    elif (clicked.get() == list[1]):
        start, stop, res, steps, B = Gauss_Jordan.Gauss_Jordan(A, X, noVar,precision.get())

    if (clicked.get() == list[2]):
        start, stop, res, steps, B = LU.LUDecomp(A, X, noVar,precision.get())
    elif not itrat and (clicked.get()==list[3] or clicked.get()==list[4]):  # clicked.get()==list[3] or clicked.get()==list[4]):
        no_iteration_lab = Label(top, text="\n\n\nnumber of iteration")
        no_iteration = Scale(top, from_=2, to=1000, orient=HORIZONTAL)
        eps_lab = Label(top, text="epsilon value")
        eps = Entry(top)
        guess_lab = Label(top, text="guess value")
        guess = Entry(top)
        no_iteration_lab.grid(row=0)
        no_iteration.grid(row=1)
        eps_lab.grid(row=2)
        eps.grid(row=3)
        guess_lab.grid(row=4)
        guess.grid(row=5)
        solv = Button(top, text="ok", command=lambda: itrative(eps, guess, top, no_iteration))
        solv.grid()
        return
    else:
        if itrat:
            if clicked.get() == list[3]:
                start, stop, c, B, res, steps = Gauss_Seidel.Gauss_Seidel(A, X, noVar, arr, ep, int(noItreation),precision.get())
            else:
                start, stop, B, res, steps = Jacobi_Iterative.Jacobi_Iterative(A, X, noVar, arr, ep, int(noItreation),precision.get())
            itrat = False
    #print("Time in seconds: %.10f" % start)
    #print("Time in seconds: %.10f" % stop)
    # print(start.10f)
    element = "Start time: " + str(start) + " End time: " + str(stop)
    element += "\nElapsed time during the whole function is : " + str(stop - start) + "\n"

    for i in range(len(res)):
        element += "x" + str(i + 1) + " = " + str(res[i])
        if (i != noVar - 1):
            element += ", "
    if clicked.get() == list[3]:
        element += '\n\n' + "Gauss Seidel error :" + str(B) + "\n\nno. of iterations:" + str(c)
        l9 = Label(top, text=element)
        l9.grid(row=0)
        num = Label(top, text=str(counter) + " of " + str(c))
        f = True
    elif clicked.get() == list[4]:
        element += '\n\n' + "Jacobi Iterative error:" + str(B) + "\n\nno. of iterations:" + str(c)
        l9 = Label(top, text=element)
        l9.grid(row=0)
        num = Label(top, text=str(counter) + " of " + str(c))
        f=True
    else:
        num = Label(top, text=str(counter) + " of " + str(len(steps)))
    l9 = Label(top, text=element)
    l9.grid(row=0)
    num.grid(row=2, column=1)
    Back = Button(top, text="preivios", command=lambda: print_res(top, 0,f))
    forward = Button(top, text="next", command=lambda: print_res(top, 1,f))
    Back.grid(row=3, column=0)
    forward.grid(row=3, column=2)
    print_res(top, 2,f)
    end = Button(top, text="exit", command=lambda: dest(top))
    end.grid(row=3,column=1)
    submit.forget()
    # Gauss_Seidel.Gauss_Seidel(A,X,noVar)


def equation_inbut():
    global i
    global equation_lab, submit, equation
    if not valid(equation.get()):
        return
    i += 1
    equation_lab.forget()
    submit.forget()
    equation.forget()
    drop.forget()
    if (i % 10 == 1):
        equation_lab = Label(root, text="Enter the " + str(i) + "st equation")
    elif (i % 10 == 2):
        equation_lab = Label(root, text="Enter the " + str(i) + "nd equation")
    elif (i % 10 == 3):
        equation_lab = Label(root, text="Enter the " + str(i) + "rd equation")
    else:
        equation_lab = Label(root, text="Enter the " + str(i) + "th equation")
    if (i != noVar + 1):
        equation.delete(0, 'end')
        equation_lab.pack()
        equation.pack()
        submit.pack()
    else:
        precision_lab.pack()
        precision.pack()
        drop.pack()
        submit = Button(root, text="Solve", command=solve)
        submit.pack()


def number_inbut():
    global equation_lab, submit, noVar, A, X, drop
    # equation_lab = Label(root,text = "Enter the "+ str(1) +"st equation" ).pack()
    no_var_lab.forget()
    no_var.forget()
    ok.forget()
    noVar = no_var.get()
    A = [[0.0] * noVar] * noVar
    X = [0.0] * noVar
    submit = Button(root, text="Enter", command=equation_inbut)
    equation_lab = Label(root, text="Enter the " + str(i) + "st equation")
    equation_lab.pack()
    equation.pack()
    submit.pack()
    # drop.pack()


ok = Button(root, text="OK", command=number_inbut)

# showing screen
title.pack()
no_var_lab.pack()
no_var.pack()
ok.pack()
# ok.forget()

root.mainloop()
