import math
from tkinter import *
from tkinter import messagebox

from phase_2 import Bisection, False_position, Fixed_point, newton_raphson, secant

root = Tk()
root.title("Numeric Project")
root.geometry("200x300")
# lable widget
title = Label(root, text="Numeric Project\nphase 2\n\n")
Max_Lab = Label(root, text="Max Iterations")
Max = Scale(root, from_=4, to=1000, orient=HORIZONTAL)
Max.set(50)
equation_lab = Label(root,text="equation")
precision_lab = Label(root, text="precision")
precision = Scale(root, from_=0, to=20, orient=HORIZONTAL)
eps_Lab = Label(root, text="epsilon")
eps = Entry(root)
X0_Lab = Label(root, text="X0")
X0 = Entry(root)
Xl_Lab = Label(root, text="X Lower")
Xl = Entry(root)
Xu_Lab = Label(root, text="X Upper")
Xu = Entry(root)
precision.set(0)
clicked = StringVar()
clicked.set("Bisection")
list = ['Bisection', 'False-Position', 'Fixed point', 'Newton-Raphson', 'Secant Method']
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


def fun(x, exp):
    exp = exp.lower()
    print(exp)
    x = 1
    exp = exp.replace('^', '**')
    exp = exp.replace('log', 'math.log10')

    exp = exp.replace('sin', 'math.sin')
    exp = exp.replace('cos', 'math.cos')
    exp = exp.replace('tan', 'math.tan')
    exp = exp.replace('sinh', 'math.sinh')
    exp = exp.replace('cosh', 'math.cosh')
    exp = exp.replace('tanh', 'math.tanh')

    exp = exp.replace('pi', 'math.pi')
    exp = exp.replace('e', 'math.e')
    return eval(exp)
def invalid_variable():
    messagebox.showerror("invalid variable", "invalid variable Name")


def invalid_value():
    messagebox.showerror("invalid value", "epsilon invalid")



t1 = 0
t2 = 0
numGuesses = 0
xl = 0.0
xu = 0.0
ans = 0.0
ea = 0.0
def solve ():
    top = Toplevel()
    if Xl.get() == "":
        Xl.insert(0,"0.0")
    if Xu.get() == "":
        Xu.insert(0,"0.0")
    if clicked.get() == list[0]:
        Bisection.Bisection(equation.get(),float(X0.get()),float(Xl.get()), float(Xu.get()),top,precision.get(),float(eps.get()),int(Max.get()))
    elif clicked.get() == list[1]:
        False_position.Falsi(equation.get(),float(X0.get()),float(Xl.get()), float(Xu.get()),top,precision.get(),float(eps.get()),int(Max.get()))
    elif clicked.get() == list[2]:
        Fixed_point.FixedPt(equation.get(),float(X0.get()),float(eps.get()),int(Max.get()),top,precision.get())
    elif clicked.get() == list[3]:
        newton_raphson.newton_raphson(equation.get(),float(X0.get()),float(eps.get()),int(Max.get()),top,precision.get())
    else:
        secant.secant(equation.get(),float(X0.get()),float(Xl.get()),float(eps.get()),int(Max.get()),top,precision.get())


def equation_inbut():
    ep = 0
    x0 = 0.0
    try:
        if eps.get() == "":
            eps.insert(0, "0.00001")
        else:
            ep = float(eps.get())
    except:
        invalid_value()
        return
    try:
        if X0.get() == "":
            X0.insert(0,"0.0")
        else:
            x0 = float(X0.get())
    except:
        messagebox.showerror("invalid value", "X0 invalid")
        return
    try:
        x = equation.get().split('=')
        if len(x)!=2:
            print(int(""))
        fun(x0 ,x[0])
    except:
        messagebox.showerror("invalid value", "equation invalid")
        return
    eps_Lab.forget()
    eps.forget()
    equation_lab.forget()
    equation.forget()
    X0.forget()
    X0_Lab.forget()
    Max.forget()
    Max_Lab.forget()
    ok.forget()
    precision_lab.pack()
    precision.pack()
    Xl_Lab.pack()
    Xl.pack()
    Xu_Lab.pack()
    Xu.pack()
    drop.pack()
    solve_button = Button(text="solve",command=solve)
    solve_button.pack()

ok = Button(root, text="OK", command=equation_inbut)

# showing screen
title.pack()
Max_Lab.pack()
Max.pack()
equation_lab.pack()
equation.pack()
eps_Lab.pack()
eps.pack()
X0_Lab.pack()
X0.pack()
ok.pack()

root.mainloop()
