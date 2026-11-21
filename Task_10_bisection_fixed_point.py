import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root_scalar

# Thermal balance model:
# f(T) = 0 means net thermal gain equals loss.
def heat_balance(T):
    return T - 20 - 8 * np.exp(-T / 18)


# Bisection: bracket a sign change
solution = root_scalar(
    heat_balance,
    bracket=[15, 35],
    method="bisect",
    xtol=1e-10
)

# Fixed-point form:
# T = 20 + 8 * exp(-T / 18)
def g(T):
    return 20 + 8 * np.exp(-T / 18)


T = 25.0
history = [T]
for _ in range(100):
    T_new = g(T)
    history.append(T_new)
    if abs(T_new - T) < 1e-10:
        break
    T = T_new

print(f"Bisection equilibrium temperature: {solution.root:.6f} C")
print(f"Fixed-point equilibrium temperature: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history) - 1)

temps = np.linspace(15, 35, 300)
plt.plot(temps, heat_balance(temps))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)")
plt.ylabel("Thermal-balance function")
plt.title("Equilibrium temperature")
plt.grid(True)
plt.show()