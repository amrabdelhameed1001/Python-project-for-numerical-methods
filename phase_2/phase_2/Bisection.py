import math
import time
from tkinter import Label, messagebox
import numpy as geek
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pylab import plot,show,axvline,axhline

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

def Bisection(exp, x, xl, xu,top,pre, es=1e-5, maxIterations=50 ):
    t1 = time.time()
    ea = 1
    res = ""
    numGuesses = 1
    x_r = []
    x_l = []
    x_u = []
    ans = (xu + xl) / 2.0
    x_r.append(ans)
    x_u.append(xu)
    x_l.append(xl)

    if fun(xl, exp) * fun(xu, exp) > 0:
        res += "no bracket"
        messagebox.showerror("invalid value", res)
        top.destroy()
        return
        #print('\nno bracket')


    res += "\nThe Bisection Method:"
    #print("The Bisection Method:")
    while ea >= es and numGuesses <= maxIterations:
        res += '\n%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%' % (numGuesses, xl, xu, ans, ea*100)
        #print('%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%' % (numGuesses, xl, xu, ans, ea*100))
        numGuesses += 1
        if fun(xl, exp) * fun(ans, exp) < 0:
            ans = precision.precision(ans,pre)
            xu = ans
            x_u.append(xu)
        elif fun(xl, exp) * fun(ans, exp) > 0:
            xl = ans
            xl = precision.precision(xl,pre)
            x_l.append(xl)
        else:
            break
        temp = precision.precision((xu + xl) / 2.0,pre)
        ea = precision.precision(abs((temp -ans) / temp),pre)
        ans = temp
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"
    element += '\n%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%\n' % (numGuesses, xl, xu, ans, ea*100)
    element += '\nnumGuesses = ' + str(numGuesses)
    element += "\n" + str(ans) + "is close to solution with equation = " + str(x) + "\n"
    #print('%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%\n' % (numGuesses, xl, xu, ans, ea*100))
    #print('numGuesses =', numGuesses)
    #print(ans, 'is close to solution with equation =', x, "\n")
    l9 = Label(top, text=element + res)
    l9.pack()
    x = geek.linspace(x_l[0], x_u[0],100, endpoint=True)
    y = fun(x, exp)
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)
    plot1.plot(x, y)
    plot1.axvline(x = x_l[0], color = 'g')
    plot1.axvline(x = ans, color = 'r')
    plot1.axvline(x = x_u[0], color = 'y')
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