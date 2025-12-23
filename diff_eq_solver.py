import matplotlib.pyplot as plt
import numpy as np

def diff_eq_function(x: float, y: float) -> float:
    return np.cos(x*y) #TODO: change this function to your desired function

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
    V = diff_eq_function(X, Y)

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
            k2 = diff_eq_function(x+step/2, y+k1*step/2)
            k3 = diff_eq_function(x+step/2, y+k2*step/2)
            k4 = diff_eq_function(x+step, y+k3*step)

            y = y + step * (k1 + 2*k2 + 2*k3 + k4)/6
            x = x + step
            
    elif x > final_x:
        while x > final_x:
            k1 = diff_eq_function(x, y)
            k2 = diff_eq_function(x+step/2, y+k1*step/2)
            k3 = diff_eq_function(x+step/2, y+k2*step/2)
            k4 = diff_eq_function(x+step, y+k3*step)

            y = y - step * (k1 + 2*k2 + 2*k3 + k4)/6
            x = x - step
    else:
        return initial_cond[1]
    
    return y

def solve(initial_cond: list[float], 
                   rangex: list[float, float], 
                   rangey: list[float, float]) -> None:
    
    """Create matplotlib plots that shows a numerical solution to first-order differential equation
    for a given range, alongside a direction field.

    initial_cond: initial conditions in (x, y) format
    rangex: range of the x-axis
    rangey: range of the y-axis"""

    x_values = np.linspace(rangex[0], rangex[1], 1000)

    print("Calculating values...")
    y_values_euler = [euler(initial_cond, i) for i in x_values]
    y_values_improved_euler = [improved_euler(initial_cond, i) for i in x_values]
    y_values_rk4 = [runge_kutta_4(initial_cond, i) for i in x_values]

    print("Plotting...")
    plt.plot(x_values, y_values_euler, label = 'euler')
    plt.plot(x_values, y_values_improved_euler, label = 'heun')
    plt.plot(x_values, y_values_rk4, label = 'rk4')

    # The following prevents the y-axis from blowing up due to function
    # ylim_fixer prevents cutting off direction field arrows
    ylim_fixer = (rangey[1]-rangey[0])*0.05
    plt.ylim(rangey[0]-ylim_fixer, rangey[1]+ylim_fixer)

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    
    dir_field = direction_field(rangex, rangey)
    plt.quiver(dir_field[0], dir_field[1], dir_field[2], dir_field[3])
    plt.legend()
    print("Done.")
    plt.show()

solve([0, 2], [-4, 4], [-4, 4]) #TODO: change initial value and axes ranges to your choice
