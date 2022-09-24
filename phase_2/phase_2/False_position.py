import math
import time
from tkinter import messagebox, Label
import numpy as geek
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from phase_2 import precision


def fun(x, exp):
    exp = exp.lower()

    exp = exp.replace('^', '**')
    exp = exp.replace('=', '-')
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

def Falsi(exp, x, xl, xu, top,pre,es=1e-5, maxIterations=50):
    t1 = time.time()
    ea = 1
    r = []
    l = []
    u = []

    ans = precision.precision((xl*fun(xu, exp) - xu*fun(xl, exp)) / (fun(xu, exp) - fun(xl, exp)),pre)
    r.append(ans)
    numGuesses = 1
    res =""
    if fun(xl, exp) < 0 and fun(xu, exp) > 0:
        pass
    elif fun(xl, exp) >= 0 and fun(xu, exp) <= 0:
        xl, xu = xu, xl
    else:
        res += 'No root can be found!'
        messagebox.showerror("invalid value", res)
        top.destroy()
        #print('No root can be found!')
        return
    u.append(xu)
    l.append(xl)
    print("The False-Position Method:")
    res += "The False-Position Method:"
    while ea >= es and numGuesses <= maxIterations:
        res += '%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%' % (numGuesses, xl, xu, ans, ea*100)
        print('%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%' % (numGuesses, xl, xu, ans, ea*100))
        numGuesses += 1
        if fun(ans, exp) < 0:
            ans = precision.precision(ans,pre)
            xl = ans
        elif fun(ans, exp) > 0:
            xu = ans
            xu = precision.precision(xu,pre)
        else:
            break
        temp = precision.precision((xl*fun(xu, exp) - xu*fun(xl, exp)) / (fun(xu, exp) - fun(xl, exp)),pre)
        ea = precision.precision(abs((temp -ans) / temp),pre)
        ans = temp
        r.append(ans)
        u.append(xu)
        l.append(xl)
    element = "Start time: " + str(t1) + " End time: " + str(time.time())
    element += "\nElapsed time during the whole function is : " + str(t1 - time.time()) + "\n"
    element += '\n%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%\n' % (numGuesses, xl, xu, ans, ea*100)
    element += '\nnumGuesses = ' + str(numGuesses)
    element += "\n" + str(ans) + "is close to solution with equation = " + str(x) + "\n"
    print('%.2d. xl = %.6f\txu = %.6f\tans = %.6f\tEa = %.6f%%\n' % (numGuesses, xl, xu, ans, ea*100))
    print('numGuesses =', numGuesses)
    print(ans, 'is close to solution with equation =', x, "\n")
    l9 = Label(top, text=element + res)
    l9.pack()
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
    plot1 = fig.add_subplot(111)
    for i in range(len(r)):

        x = geek.linspace(l[i], u[i],5, endpoint=True)
        z = fun(x, exp)
        plot1.plot(x, z)
        w = fun(l[i], exp)
        c = fun(u[i], exp)
        x_slope = [l[i], u[i]] #in case False-Position we plot a line between Xu and Xl to get Xr
        y_slope = [w, c] #these two lines represtns the co-ordinaiton of 2 points of the line bewteen Xr and Xl
        plot1.plot(x_slope, y_slope, color = 'g')
        plot1.axhline(y=0, color = 'black')
        #in case False-Position we plot a line between Xu and Xl to get Xr

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