import numpy as np
from scipy.integrate import simpson

# Pump flow-rate readings taken every two hours
time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
flow_m3_h = np.array([1.2, 1.5, 2.0, 2.4, 2.1, 1.6, 1.1])

volume_trapezoid = np.trapezoid(flow_m3_h, time_hours)
volume_simpson = simpson(flow_m3_h, x=time_hours)

print(f"Volume using trapezoidal rule: {volume_trapezoid:.3f} m^3")
print(f"Volume using Simpson's rule: {volume_simpson:.3f} m^3")
print(f"Difference between estimates: {abs(volume_simpson - volume_trapezoid):.3f} m^3")