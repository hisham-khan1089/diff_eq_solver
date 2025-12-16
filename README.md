# First Order Differential Equation Solver

## General Information
diff_eq_solver.py is a simple script that takes a first-order differential equation of the form dy/dx = f(x,y)
and solves it numerically. 

The goal of this project was to compare some numerical methods (Euler's, Improved Euler's, RK4) side-by-side
on real differential equations to see how they diverge.

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
