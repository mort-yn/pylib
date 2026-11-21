from scipy.optimize import minimize

# x = number/capacity units of Type A pool
# y = number/capacity units of Type B pool
#
# Cost per unit: A = 15, B = 22
# Capacity per unit: A = 120, B = 200
# Required total capacity: at least 1200
def cost(z):
    x, y = z
    return 15 * x + 22 * y


def capacity_constraint(z):
    x, y = z
    return 120 * x + 200 * y - 1200


constraints = {
    "type": "ineq",
    "fun": capacity_constraint
}
bounds = [(0, None), (0, None)]

solution = minimize(
    cost,
    x0=[5, 3],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

x, y = solution.x
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {120 * x + 200 * y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# If whole units are required, test nearby integer combinations.
best_integer = None
for a in range(0, 21):
    for b in range(0, 21):
        capacity = 120 * a + 200 * b
        if capacity >= 1200:
            total_cost = 15 * a + 22 * b
            if best_integer is None or total_cost < best_integer[0]:
                best_integer = (total_cost, a, b, capacity)

print("Best nearby integer solution:", best_integer)