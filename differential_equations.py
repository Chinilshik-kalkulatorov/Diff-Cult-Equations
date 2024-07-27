import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def input_differential_equation():
    print("Enter the coefficients for the differential equation dy/dt = a*y + b:")
    a = float(input("a: "))
    b = float(input("b: "))
    return a, b

def solve_first_order_ode(a, b, y0, t):
    def model(y, t):
        return a * y + b

    y = odeint(model, y0, t)
    return y

def solve_second_order_ode(a, b, c, y0, y1, t):
    def model(Y, t):
        y, dy = Y
        d2y = a * y + b * dy + c
        return [dy, d2y]

    Y0 = [y0, y1]
    Y = odeint(model, Y0, t)
    return Y[:, 0]

def main():
    print("Choose the type of differential equation to solve:")
    print("1. First-order linear ODE (dy/dt = a*y + b)")
    print("2. Second-order linear ODE (d2y/dt2 = a*y + b*dy + c)")
    choice = int(input("Enter 1 or 2: "))

    t = np.linspace(0, 10, 100)
    
    if choice == 1:
        a, b = input_differential_equation()
        y0 = float(input("Enter the initial condition y(0): "))
        y = solve_first_order_ode(a, b, y0, t)
        plt.plot(t, y)
        plt.xlabel('t')
        plt.ylabel('y(t)')
        plt.title('Solution of First-order ODE')
        plt.show()

    elif choice == 2:
        print("Enter the coefficients for the differential equation d2y/dt2 = a*y + b*dy + c:")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        y0 = float(input("Enter the initial condition y(0): "))
        y1 = float(input("Enter the initial condition dy/dt(0): "))
        y = solve_second_order_ode(a, b, c, y0, y1, t)
        plt.plot(t, y)
        plt.xlabel('t')
        plt.ylabel('y(t)')
        plt.title('Solution of Second-order ODE')
        plt.show()
    else:
        print("Invalid choice.")

if name == "__main__":
    main()
