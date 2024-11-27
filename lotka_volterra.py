import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lotka-Volterra equations
def lotka_volterra(t, z, alpha, beta, delta, gamma):
    x, y = z  # Unpack prey and predator populations
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Parameters
alpha = 0.13  # Prey birth rate
beta = 0.023  # Predator-prey interaction rate
delta = 0.011 # Predator reproduction rate per prey eaten
gamma = 0.12  # Predator death rate

# Initial conditions
x0 = 40  # Initial prey population
y0 = 1   # Initial predator population
z0 = [x0, y0]

# Time span for the simulation
t_span = (0, 100)  # Time range for simulation
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Time points to evaluate solution

# Solve the system of differential equations
sol = solve_ivp(
    lotka_volterra, t_span, z0, args=(alpha, beta, delta, gamma), t_eval=t_eval
)


# Plotting the results

## Plot prey and predator populations over time
#plt.figure(figsize=(12, 5))
#plt.plot(sol.t, sol.y[0], label="Prey Population (x)", color="b")
#plt.plot(sol.t, sol.y[1], label="Predator Population (y)", color="r")
#plt.xlabel("Time")
#plt.ylabel("Population")
#plt.title("Lotka-Volterra Predator-Prey Model")
#plt.legend()
#plt.grid()
#plt.show()

# Optional: Phase plot of prey vs predator
plt.figure(figsize=(6, 5))
plt.plot(sol.y[0], sol.y[1], color="purple")
plt.xlabel("Prey Population (x)")
plt.ylabel("Predator Population (y)")
plt.title("Phase Plot of Prey vs Predator")
plt.grid()
plt.show()
