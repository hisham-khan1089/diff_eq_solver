# First Order Differential Equation Solver

## General Information
diff_eq_solver.py is a simple script that takes a first-order differential equation of the form dy/dx = f(x,y)
and solves it numerically. 

The goal of this project was to compare some numerical methods (Euler's, Improved Euler's, RK4) side-by-side
on real differential equations to see if and how they diverge.

## Setup 
### Prerequisites

- **Python 3.8+** with pip
1. **Create and activate a virtual environment:**

   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r dev-requirements.txt
   ```

## Using the Script
The script is present in diff_eq_solver.py.
- Edit differential equation
   - diff_eq_function is the function that represents the f(x,y) in dy/dx = f(x,y).
   - Edit the output of this function to edit your differential equation.
- Creating the plot
  - diff_eq_solver is the function that does all the work to solve and plot the solution.
  - The first argument is the initial condition (a point that satisfies the equation).
  - The second two arguments are the x and y ranges. Once you run the script, a matplotlib plot will appear showing the solutions using various numerical methods.
   
