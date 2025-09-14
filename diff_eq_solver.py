import matplotlib.pyplot as plt
import numpy as np
import math

def diff_eq_function(x: float, y: float) -> float:
    return math.sin(y)

diff_eq_function_np = np.vectorize(diff_eq_function)

def direction_field(range: list[float, float], n: int | None = None) -> list[list]:
    """Generates the meshgrids (matrices) used to create a direction field of 
    a given first-order differential equation using plt.quiver.
    
    range: two item list representing the range on both the x- and y-axis of the
    direction field
    n: the number of directions shown per dimension (x and y)"""

    if n == None:
        n = 20
    x = np.linspace(range[0], range[1], n)
    y = np.linspace(range[0], range[4], n)

    X, Y = np.meshgrid(x, y) 
    
    U = 1
    V = diff_eq_function_np(X, Y)

    U = U/np.sqrt(U**2 + V**2)
    V = V/np.sqrt(U**2 + V**2)

    return list(X, Y, U, V)

def euler(initial_cond: list[float], step: float, final_x: float) -> float:
    x = initial_cond[0]
    y = initial_cond[1]

    while x < final_x:
        y = y + step * diff_eq_function(x, y)
        x = x + step
     
    return y
    


plt.subplots


    
plt.quiver()
plt.show()
