import math
import time
from tkinter import Label

import numpy as geek
import matplotlib.pyplot
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pylab import plot,show
from numpy import array,linspace,sqrt,sin
from numpy.linalg import norm

from phase_2 import precision


def g(x,exp):
    #exp = "3 / (x - 2)"
    exp = exp.lower()

    exp = exp.replace('^', '**')
    exp = exp.replace('=x', '')
    exp = exp.replace('= x', '')
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


def FixedPt(exp,x0, es, iter_max,top,pre):
    t1 = time.time()
    xp = []               #array to store estimated root in each step
    xr = x0                #Estimated root
    xp.append(xr)          #Keep xr from previous iteration
    iter = 0                #Keep track of # of iterations
    res = ""
    while True:
        xr_old = xr
        xr = g(xr_old,exp)
        xr = precision.precision(xr,pre)
        xp.append(xr)
        ea = precision.precision(abs((xr - xr_old)),pre)
        iter += 1
        res += "\nIteration" + str(iter) +"\nxi: " + str(xr)
        if (iter > 1):
            res += "\nApproximation error: " + str(ea) + "\n"
            print(" Approximation error: ", ea, "\n")
        if (ea <= es or iter >= iter_max or abs(xr) > (2 ** 31 - 1)):
            break
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"
    l9 = Label(top, text=element + res)
    l9.pack()
    ans = []
    for i in xp:
        z = g(i,exp)
        ans.append(z)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)
    x = geek.linspace(0, 5,100, endpoint=True)
    y = g(x,exp)
    plot1.plot(x, y, xp, ans, 'bo', x0, g(x0,exp), 'ro', xr, g(xr,exp), 'go', x, x, 'k')
    plot1.axhline(y=0, color = 'black')
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
    if iter >= iter_max or abs(xr) > (2 ** 31 - 1):
        return "No fixed point for given start value", xp, 0









