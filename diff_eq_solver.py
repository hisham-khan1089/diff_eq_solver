import matplotlib.pyplot as plt
import numpy as np
import math

def diff_eq_function(x: float, y: float) -> float:
    return 1/(1+x**2-y**2) #TODO: change this function to your desired function

diff_eq_function_np = np.vectorize(diff_eq_function)

def direction_field(rangex: list[float, float], 
                    rangey: list[float, float], 
                    n: int | None = None) -> list[list]:
    
    """Generates the meshgrids (matrices) used to create a direction field of 
    a given first-order differential equation using plt.quiver.
    
    rangex: range of the x-axis
    rangey: range of the y-axis
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

def euler(initial_cond: list[float], 
          final_x: float, 
          step: float | None = None) -> float:
    
    """Use Euler's method to approximate and return a numerical solution to a first-order 
    differential equation for a given x-value and given an initial value.
    
    initial_cond: list containing initial value [x, y]
    final_x: the x-value to approximate
    step: step size"""
    
    if step == None:
        step = 0.005

    x = initial_cond[0]
    y = initial_cond[1]

    if x < final_x:
        while x < final_x:
            y = y + step * diff_eq_function(x, y)
            x = x + step
    elif x > final_x:
        while x > final_x:
            y = y - step * diff_eq_function(x, y)
            x = x - step
    else:
        return initial_cond[1]
    
    return y

def improved_euler(initial_cond: list[float], 
                   final_x: float, 
                   step: float | None = None) -> float:

    """Use Improved Euler's method to approximate and return a numerical solution to a first-order 
    differential equation for a given x-value and given an initial value.
    
    initial_cond: list containing initial value [x, y]
    final_x: the x-value to approximate
    step: step size"""

    if step == None:
        step = 0.005

    x = initial_cond[0]
    y = initial_cond[1]

    if x < final_x:
        while x < final_x:
            g1 = diff_eq_function(x, y)
            g2 = diff_eq_function(x+step, y+step*g1)

            y = y + step * (g1+g2)/2
            x = x + step

    elif x > final_x:
        while x > final_x:
            g1 = diff_eq_function(x, y)
            g2 = diff_eq_function(x+step, y+step*g1)

            y = y - step * (g1+g2)/2
            x = x - step
    else:
        return initial_cond[1]
    
    return y
    
def runge_kutta_4(initial_cond: list[float], 
                   final_x: float, 
                   step: float | None = None) -> float:

    """Use Runge-Kutta 4 to approximate and return a numerical solution to a first-order 
    differential equation for a given x-value and given an initial value.
    
    initial_cond: list containing initial value [x, y]
    final_x: the x-value to approximate
    step: step size"""

    if step == None:
        step = 0.005

    x = initial_cond[0]
    y = initial_cond[1]

    if x < final_x:
        while x < final_x:
            k1 = diff_eq_function(x, y)
            k2 = diff_eq_function(x+step/2, y+step/2*k1)
            k3 = diff_eq_function(x+step/2, y+step/2*k2)
            k4 = diff_eq_function(x+step, y+step*k3)

            y = y + step * (k1 + 2*k2 + 2*k3 + k4)/6
            x = x + step
            
    elif x > final_x:
        while x > final_x:
            k1 = diff_eq_function(x, y)
            k2 = diff_eq_function(x+step/2, y+step/2*k1)
            k3 = diff_eq_function(x+step/2, y+step/2*k2)
            k4 = diff_eq_function(x+step, y+step*k3)

            y = y - step * (k1 + 2*k2 + 2*k3 + k4)/6
            x = x - step
    else:
        return initial_cond[1]
    
    return y

def diff_eq_solver(initial_cond: list[float], 
                   rangex: list[float, float], 
                   rangey: list[float, float]) -> None:
    
    """Create matplotlib plots that shows a numerical solution to first-order differential equation
    for a given range, alongside a direction field.

    initial_cond: initial conditions in (x, y) format
    rangex: range of the x-axis
    rangey: range of the y-axis"""

    x_values = np.linspace(rangex[0], rangex[1], 100)

    y_values_euler = []
    y_values_improved_euler = []
    y_values_rk4 = []

    for i in x_values:
        y_values_euler.append(euler(initial_cond, i))
        y_values_improved_euler.append(improved_euler(initial_cond, i))
        y_values_rk4.append(runge_kutta_4(initial_cond, i))

    y_values_euler = np.array(y_values_euler)
    y_values_improved_euler = np.array(y_values_improved_euler)
    y_values_rk4 = np.array(y_values_rk4)

    plt.plot(x_values, y_values_euler, label = 'euler')
    plt.plot(x_values, y_values_improved_euler, label = 'heun')
    plt.plot(x_values, y_values_rk4, label = 'rk4')

    # Prevents y axes from blowing up due to function
    # Also does so without cutting off direction field arrows (hence ylim_fixer)

    ylim_fixer = (rangey[1]-rangey[0])*0.05
    plt.ylim(rangey[0]-ylim_fixer, rangey[1]+ylim_fixer)

    dir_field = direction_field(rangex, rangey)
    plt.quiver(dir_field[0], dir_field[1], dir_field[2], dir_field[3])
    plt.legend()
    plt.show()

diff_eq_solver([0, 2], [-5, 5], [-5, 5])
