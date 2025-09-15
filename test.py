import math

def diff_eq_function(x: float, y: float) -> float:
    return math.sin(y)

def euler(initial_cond: list[float], final_x: float, n: float | None = None) -> float:
    
    """Use Euler's method to approximate and return a numerical solution to a first-order 
    differential equation for a given x-value given an initial value.
    
    initial_cond: list containing ordered (x, y) pair initial value
    step: step size for Euler's method
    final_x: the x-value to approximate"""
    
    if n == None:
        n = 10
    
    x = initial_cond[0]
    y = initial_cond[1]

    step = (final_x - x)/n

    while x < final_x:
        y = y + step * diff_eq_function(x, y)
        x = x + step
     
    return y

print(euler([0, 1], 2))