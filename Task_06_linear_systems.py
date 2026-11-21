import numpy as np

# x = number of Worker containers
# y = number of Database containers
# Worker uses 3 Gbps bandwidth and 50 GB storage
# Database uses 5 Gbps bandwidth and 120 GB storage
# Total observed usage: 31 Gbps bandwidth and 660 GB storage
A = np.array([
    [3.0, 5.0],
    [50.0, 120.0]
])
b = np.array([31.0, 660.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Worker containers: {solution[0]:.0f}")
print(f"Database containers: {solution[1]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))