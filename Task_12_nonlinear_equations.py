from scipy.optimize import root

# Find intersections of:
# Circle: x^2 + y^2 = 9
# Parabola: y = x^2 - 2
def equations(z):
    x, y = z
    return [
        x**2 + y**2 - 9.0,
        y - (x**2 - 2.0)
    ]


for guess in ([1.5, 1.5], [-1.5, 1.5]):
    solution = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", solution.x)
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print()