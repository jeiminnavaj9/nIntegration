# eulers.py
# script to compute:
# 1. y(x) from f(x) = dy/dx
# 2. Y(x, y) from F(x, y) = dx/dt and G(x, y) = dy/dt using
# Euler's method

# author:      Jeimin Garibnavajwala
# email:       janavaj@bu.edu
# affiliation: Boston University
# date:        March 03, 2021

# define functions here
# ============================================ #
# define iterative function to compute y(x) from dy/dx = f(x, y)
def Euler1D(derivative, x0, y0, stepSize, steps):
    """returns a list of x, and y values calculated
    iteratively using Euler's method

    parameter: derivative; dy/dx function
    parameter: x0; initial x value; x(var0) = x0
    parameter: y0; initial y value; y(var0) = y0
    parameter: stepSize; delta_x; the amount by which
               x to be increased (or decreased)
    parameter: steps; number of x, and y values to be calculated
    """
    # initialize x, and y with their initial values
    x = [x0]; y = [y0]

    # iteratively calculate x, and y
    for i in range(steps):
        y += [y[-1] + (derivative(x[-1], y[-1])*stepSize)]
        x += [x[-1] + stepSize]

    return x, y

# define iterative function to compute x and y from Y'(x, y)
def Euler2D(x_derivative, y_derivative, var0, x0, y0, stepSize, steps):
    """ returns a list of var, x, and y values calculated
    iteratively using Euler's method

    parameter: x_derivative; dx/d(var) function
    parameter: y_derivative; dy/d(var) function
    parameter: var0; initial value for the variable **var**
    parameter: x0; initial x value; x(var0) = x0
    parameter: y0; initial y value; y(var0) = y0
    parameter: stepSize; delta_var; the amount by which
               var to be increased (or decreased)
    parameter: steps; number of var, x, and y values to be calculated
    """
    # initialize var, x, and y with their initial values
    var = [var0]; x = [x0]; y = [y0]

    # iteratively calculate var, x, and y
    for i in range(steps):
        var += [var[-1] + stepSize]
        x += [x[-1] + (x_derivative(x[-1], y[-1])) * stepSize]
        y += [y[-1] + (y_derivative(x[-1], y[-1])) * stepSize]

    return var, x, y
# ============================================ #

