# Numerical First-Order Differential Equation Solver

This is a mini project that takes a first-order differential equation of the form dy/dx = f(x,y)
and solves it numerically. The goal of this project was to compare some numerical methods (Euler's, 
Improved Euler's, RK4) side-by-side on real differential equations to see if and how they diverge.

The script is in `diff_eq_solver.py`.

### Using the script
Edit the output of the function `diff_eq_function` to alter f(x,y).

The `solve` function does the final plotting work. 
- The first argument is the initial condition coordinate
- The second and third arguments are the x- and y-axis ranges, respectively

Once you run the script, a Matplotlib plot will show the colour-coded numerical solutions.
