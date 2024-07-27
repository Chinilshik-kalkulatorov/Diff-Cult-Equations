# Diff-Cult-Equations
## Differential Equations with Checkmarks and Crosses

This project contains Python code for solving basic differential equations using SciPy. The user can input the coefficients and initial conditions for the differential equations from the keyboard. The script also provides visual plots of the solutions.

## Operations Included

1. Solving a first-order linear differential equation (dy/dt = a*y + b)
2. Solving a second-order linear differential equation (d2y/dt2 = a*y + b*dy + c)

## How to Use

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/Diff-Cult-Equations.git
    ```

2. Navigate to the project directory:
    ```
    cd Diff-Cult-Equations
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the Python script:
    ```
    python differential_equations.py
    ```

5. Follow the prompts to input the coefficients and initial conditions for the differential equations. The script will then display a plot of the solution.

## Example

After running the script, you will be prompted to enter the coefficients and initial conditions for the differential equations. The script will then display a plot of the solution.

### Sample Input for First-order ODE
```
Choose the type of differential equation to solve:
1. First-order linear ODE (dy/dt = a*y + b)
2. Second-order linear ODE (d2y/dt2 = a*y + b*dy + c)
Enter 1 or 2: 1
Enter the coefficient a: 1
Enter the coefficient b: 2
Enter the initial condition y(0): 0
```

### Sample Output for First-order ODE
For the input coefficients a = 1, b = 2, and the initial condition y(0) = 0, the solution of the first-order differential equation dy/dt = y + 2 is:
```
y(t) = 2(e^t - 1)
```
The plot of this solution over time is saved as `sample_output_first_order.png`.


### Sample Input for Second-order ODE
```
Choose the type of differential equation to solve:
1. First-order linear ODE (dy/dt = a*y + b)
2. Second-order linear ODE (d2y/dt2 = a*y + b*dy + c)
Enter 1 or 2: 2
Enter the coefficient a: 1
Enter the coefficient b: -2
Enter the coefficient c: 1
Enter the initial condition y(0): 0
Enter the initial condition dy/dt(0): 1
```

### Sample Output for Second-order ODE
For the input coefficients a = 1, b = -2, c = 1, and the initial conditions y(0) = 0 and dy/dt(0) = 1, the solution of the second-order differential equation d2y/dt2 = y - 2*dy/dt + 1 is:
```
y(t) = e^t - t - 1
```
The plot of this solution over time is saved as `sample_output_second_order.png`.
![combined_ode_solutions_side_by_side](https://github.com/user-attachments/assets/e627bfe2-1d73-4d25-bb8d-af86bc6a065a)

## Dependencies

- Python 3.x
- NumPy 1.21.0
- SciPy 1.7.1
- Matplotlib 3.4.3

Install the dependencies using pip:
```
pip install numpy==1.21.0 scipy==1.7.1 matplotlib==3.4.3
```

## License

This project is licensed under the MIT License.
