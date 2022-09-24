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

    exp = exp.replace('sin', 'math.sin')
    exp = exp.replace('cos', 'math.cos')
    exp = exp.replace('tan', 'math.tan')
    exp = exp.replace('sinh', 'math.sinh')
    exp = exp.replace('cosh', 'math.cosh')
    exp = exp.replace('tanh', 'math.tanh')

    exp = exp.replace('pi', 'math.pi')
    exp = exp.replace('e', 'math.e')
    exp = exp.replace('=', '-')
    return eval(exp)

def secant(exp, x0, x1, tolerance , mx_iterations,top,pre):
    t1 = time.time()
    error = 1
    i = 1
    x = sym.symbols('x')
    res = ""
    while (error > tolerance and i <= mx_iterations):

        f0_subs = precision.precision(fun(x0, exp),pre)  # substitution in the function f(xi-1)
        f1_subs = precision.precision(fun(x1, exp),pre)  # substitution in the function f(xi)

        if (f0_subs - f1_subs == 0):  # divided by zero
            res += "no scant"
            messagebox.showerror("invalid value", res)
            top.destroy()
            return

        res += "\nIteration" + str(i) +"\nxi: " + str(x1)
        print("Iteration ", i, "\n")
        print(" xi: ", x1)
        if (i > 1):
            error = precision.precision(abs((x1 - x0) / x1),pre)
            res += "\nApproximation error: " + str(error) + "\n"
            print(" Approximation error: ", error, "\n")
        x1 = precision.precision(x1,pre)
        x0_next = x1
        x1 -= precision.precision((f1_subs * (x0 - x1) / (f0_subs - f1_subs)),pre)  # next x
        x0 = x0_next
        x0 = precision.precision(x0,pre)
        i += 1
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"

    l9 = Label(top, text=element + res)
    l9.pack()
    x = np.linspace(-10, 10, 100)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)

    # plot1.rcParams["figure.figsize"] = [7.50, 3.50]
    # plot1.rcParams["figure.autolayout"] = True
    plt.rcParams["figure.figsize"] = [3.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    plot1.plot(x, fun(x,exp),'r',x1,fun(x1,exp),'go')
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