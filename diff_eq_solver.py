import matplotlib.pyplot as plt
import numpy as np
import math

def diff_eq_function(x: float, y: float) -> float:
    return 100

diff_eq_function_np = np.vectorize(diff_eq_function)

def direction_field(rangex: list[float, float], rangey: list[float, float], n: int | None = None) -> list[list]:
    
    """Generates the meshgrids (matrices) used to create a direction field of 
    a given first-order differential equation using plt.quiver.
    
    range: two item list representing the range on both the x- and y-axis of the
    direction field
    n: the number of directions shown per dimension (x and y)"""

    if n == None:
        n = 20
    x = np.linspace(rangex[0], rangex[1], n)
    y = np.linspace(rangey[0], rangey[1], n)

    X, Y = np.meshgrid(x, y) 
    
    U = 1
    V = diff_eq_function_np(X, Y)

    U = U/np.sqrt(U**2 + V**2)
    V = V/np.sqrt(U**2 + V**2)

    return [X, Y, U, V]

def euler(initial_cond: list[float], final_x: float, n: float | None = None) -> float:
    
    """Use Euler's method to approximate and return a numerical solution to a first-order 
    differential equation for a given x-value and given an initial value.
    
    initial_cond: list containing initial value [x, y]
    step: step size 
    final_x: the x-value to approximate"""
    
    if n == None:
        n = 40

    x = initial_cond[0]
    y = initial_cond[1]

    step = (final_x - x)/n

    while x < final_x:
        y = y + step * diff_eq_function(x, y)
        x = x + step
     
    return y
    
def diff_eq_solver(initial_cond: list[float], rangex: list[float, float], rangey: list[float, float]) -> None:
    
    """Create matplotlib plots that shows a numerical solution to first-order differential equation
    for a given range, alongside a direction field.
    
    range: list containing lower and upper bound for both x and y axis"""

    x_values = np.linspace(rangex[0], rangex[1], 30)

    y_values = []

    for i in x_values:
        y_values.append(euler(initial_cond, i))
    
    y_values = np.array(y_values)

    plt.plot(x_values, y_values)
    ylim_fixer = (rangey[1]-rangey[0])*0.05

    # Previously the ylim was determined by the graph of the solution to the 
    # differential equation, meaning it could blow up the upper bound of the
    # y-axis.

    # This next line of code resets the bounds of the y-axis so that its upper bound
    # is slightly larger than the upper bound of range and slightly lower than the 
    # lower bound of range (so that the direction field arrows are not cut off)

    plt.ylim(rangey[0]-ylim_fixer, rangey[1]+ylim_fixer)

    dir_field = direction_field(rangex, rangey)
    plt.quiver(dir_field[0], dir_field[1], dir_field[2], dir_field[3])
    plt.show()

diff_eq_solver([0, 53], [0, 4], [0, 1000])


