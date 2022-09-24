import math
import time
from tkinter import Label, messagebox

import numpy as np
import sympy as sym


# scan input function
from matplotlib import pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from phase_2 import precision


def fun(x, exp):
    exp = exp.lower()

    exp = exp.replace('^', '**')
    exp = exp.replace('log', 'math.log10')
    exp = exp.replace('=', '-')

    exp = exp.replace('sin', 'math.sin')
    exp = exp.replace('cos', 'math.cos')
    exp = exp.replace('tan', 'math.tan')
    exp = exp.replace('sinh', 'math.sinh')
    exp = exp.replace('cosh', 'math.cosh')
    exp = exp.replace('tanh', 'math.tanh')

    exp = exp.replace('pi', 'math.pi')
    exp = exp.replace('e', 'math.e')

    return eval(exp)

def ex(exp) :
    exp = exp.lower()

    exp = exp.replace('^', '**')
    exp = exp.replace('log', 'math.log10')
    exp = exp.replace('=', '-')

    exp = exp.replace('sin', 'math.sin')
    exp = exp.replace('cos', 'math.cos')
    exp = exp.replace('tan', 'math.tan')
    exp = exp.replace('sinh', 'math.sinh')
    exp = exp.replace('cosh', 'math.cosh')
    exp = exp.replace('tanh', 'math.tanh')

    exp = exp.replace('pi', 'math.pi')
    exp = exp.replace('e', 'math.e')

    return exp

def newton_raphson(exp, xi, tolerance , mx_iterations,top,pre):
    t1 = time.time()
    error = 1
    i = 1
    x = sym.symbols('x')
    res = ""
    while (error > tolerance and i <= mx_iterations):
        res += "\nIteration " + str(i)+"\n xi: "+str(xi)
        print("Iteration ", i, "\n")
        print(" xi: ", xi)
        df = sym.diff(ex(exp), x)
        # dirivative expression of the function
        f_subs = fun(xi, exp)
        f_subs = precision.precision(f_subs,pre)
        # substitution in the function
        df_subs = fun(xi, str(df))  # substitution in the differentiation
        df_subs = precision.precision(df_subs,pre)
        if (df_subs == 0):
            res += "\nhorizontal tangent and no root"
            print("horizontal tangent and no root")
            messagebox.showerror("invalid value", res)
            top.destroy()
            return
        xi = precision.precision(xi,pre)
        xi_prev = xi

        xi -= precision.precision(f_subs / df_subs,pre)  # next x
        xi = precision.precision(xi,pre)
        if (i > 1):
            error = precision.precision(abs((xi - xi_prev) / xi),pre)
            res += "\n Approximation error: " + str(error) + "\n"
            print(" Approximation error: ", error, "\n")

        i += 1
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"
    l9 = Label(top, text=element + res)
    l9.pack()
    x = np.linspace(-10, 10, 100)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)

    plot1.plot(x, fun(x,exp),'r',xi,fun(xi,exp),'go')
    plot1.axhline(y=0, color = 'black')
    plt.show()
    canvas = FigureCanvasTkAgg(fig,
                               master = top)

    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   top)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    plt.plot(x, fun(x,exp), color='red')
    plt.show()