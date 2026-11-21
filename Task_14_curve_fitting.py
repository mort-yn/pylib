import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data batch size (MB) and measured job runtime (seconds)
batch_mb = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
runtime_s = np.array([12.0, 14.5, 18.0, 22.5, 28.0, 34.5, 42.0], dtype=float)


# A simple quadratic model for increasing processing time
def model(x, a, b, c):
    return a * x**2 + b * x + c


parameters, covariance = curve_fit(model, batch_mb, runtime_s)
a, b, c = parameters
predicted = model(batch_mb, a, b, c)
rmse = np.sqrt(np.mean((runtime_s - predicted) ** 2))

print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} s")
print(f"Predicted runtime at 400 MB: {model(400, a, b, c):.2f} s")

x_plot = np.linspace(batch_mb.min(), 400, 300)
plt.scatter(batch_mb, runtime_s, label="Measurements")
plt.plot(x_plot, model(x_plot, a, b, c), label="Fitted curve")
plt.xlabel("Batch size (MB)")
plt.ylabel("Runtime (s)")
plt.title("Job runtime curve fitting")
plt.legend()
plt.grid(True)
plt.show()