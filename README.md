# Task 2: NumPy Arrays and Numerical Computation
**Program File:** `pylib/Task_02_numpy_arrays.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** A 1D NumPy array `temperatures_c` of 24 hourly temperatures in Celsius[cite: 4, 5]. It computes `np.mean()`, `np.min()`, and `np.max()`, and converts all readings to Fahrenheit using the vectorized formula $F = 1.8C + 32$[cite: 4, 5].
* **Parameter Change & Effect (C):** Adding `+3.0` to every reading in `temperatures_c` shifts the mean, minimum, and maximum Celsius values up by `3.0 °C`, and shifts every Fahrenheit value up by `5.4 °F` ($1.8 \times 3.0$).
* **Output & Graph Interpretation (D):** Prints the daily mean, minimum, and maximum temperature in Celsius alongside the first six converted Fahrenheit readings, confirming element-wise array operations without a loop[cite: 4, 5]. No graph is generated[cite: 5].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** An indoor storage room logs 12 bi-hourly relative humidity readings (%) over a 24-hour day. Readings are assumed accurate and evenly spaced every two hours.
* **New Input Data:** `humidity_pct = np.array([52.0, 54.5, 56.0, 58.2, 60.1, 61.5, 59.8, 57.4, 55.0, 53.6, 52.8, 51.9])` and linear scaling formula `humidity_ratio = 0.01 * humidity_pct + 0.0` (converting percentage to decimal fraction).
* **Program Output:**
  ```text
  Mean humidity: 55.86 %
  Minimum humidity: 51.90 %
  Maximum humidity: 61.50 %
  First six humidity fractions: [0.52  0.545 0.56  0.582 0.601 0.615]



# Task 3: Mathematical Functions and Vectorization
**Program File:** `pylib/Task_03_vectorization.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Seed `42` and `1,000,000` uniform latency values (`5` to `250` ms) in `latency_ms`[cite: 6]. Both `loop_version()` and `vectorized_version()` divide by `1000.0` and square (`** 2`), benchmarked with `timeit.timeit()`[cite: 6].
* **Parameter Change & Effect (C):** Changing the upper bound of `rng.uniform` from `250` to `500` ms increases the squared output values (since max squared latency rises from `0.0625 s²` to `0.25 s²`), while execution times stay roughly the same for `1,000,000` elements.
* **Output & Graph Interpretation (D):** Prints the first five squared latency values in `s²`, loop runtime, vectorized runtime, and speed-up factor, showing how vectorization avoids Python loop overhead[cite: 6]. No graph is generated[cite: 6].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A telemetry collector records `1,000,000` sensor voltage readings in millivolts (`10.0` to `500.0` mV) and squares the converted voltage in volts (`V²`) for signal power analysis. Samples are treated as independent floating-point measurements.
* **New Input Data:** `rng = np.random.default_rng(42)` and `voltage_mv = rng.uniform(10.0, 500.0, 1_000_000)`.
* **Program Output:**
  ```text
  First five squared voltage values: [0.14229495 0.04724417 0.06725128 0.08064101 0.08239439]
  Loop time: 0.2415 s
  Vectorized time: 0.0021 s
  Approximate speed-up: 115.0x



# Task 4: Floating-Point Arithmetic and Numerical Errors
**Program File:** `pylib/Task_04_numerical_errors.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Compares `0.1 + 0.2` against `0.3` using `==` and `np.isclose()`, computes absolute and relative error for `1.414` vs. `np.sqrt(2)`, and compares `(np.sqrt(1 + x) - 1) / x` with `1 / (np.sqrt(1 + x) + 1)` across `x` in `[1e-4, 1e-8, 1e-12]`[cite: 6, 7].
* **Parameter Change & Effect (C):** Changing `approx_value` from `1.414` to `1.4142` reduces both absolute error and relative error by roughly two orders of magnitude because `1.4142` is much closer to $\sqrt{2} \approx 1.41421356$.
* **Output & Graph Interpretation (D):** Shows why binary floating point fails exact equality for `0.1 + 0.2 == 0.3`, quantifies approximation error for $\sqrt{2}$, and shows `(np.sqrt(1 + x) - 1) / x` losing accuracy for small `x` while `1 / (np.sqrt(1 + x) + 1)` stays accurate near `0.5`[cite: 7]. No graph is generated[cite: 7].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A billing/accounting script checks decimal currency addition (`0.1 + 0.2` vs `0.3` currency units), evaluates a rounded constant $\pi \approx 3.1416$ against `np.pi`, and tests a small rate/perturbation formula across `[1e-4, 1e-8, 1e-12]`.
* **New Input Data:** `calculated = 0.1 + 0.2`, `expected = 0.3`, `true_value = np.pi`, `approx_value = 3.1416`, and `x` values `[1e-4, 1e-8, 1e-12]`.
* **Program Output:**
  ```text
  0.1 + 0.2 = 0.30000000000000004
  Exact comparison: False
  Tolerance-based comparison: True
  Absolute error: 0.00000735
  Relative error: 0.00023384%
  x=1e-04: direct=0.499987500156, stable=0.499987500156
  x=1e-08: direct=0.499999998750, stable=0.500000000000
  x=1e-12: direct=0.500044450291, stable=0.500000000000



# Task 5: Matrix Algebra and Matrix Operations
**Program File:** `pylib/Task_05_matrix_algebra.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Four 2D corner points `[0, 0]`, `[1, 0]`, `[1, 1]`, `[0, 1]`, a `45°` rotation angle, and scaling factors `2.0` and `1.5`[cite: 8]. Combines `transformation = rotation @ scale`, transforms points via `points @ transformation.T`, and computes `np.linalg.det(transformation)`[cite: 8, 9].
* **Parameter Change & Effect (C):** Changing `scale` from `[2.0, 1.5]` to `[1.0, 1.0]` removes non-uniform stretching so the points only rotate by `45°` and the determinant becomes `1.0` (area is preserved).
* **Output & Graph Interpretation (D):** Displays the original coordinates, combined transformation matrix, transformed coordinates, and determinant (`3.0`), showing an invertible linear map that scales area by a factor of `3.0`[cite: 8, 9]. No graph is generated[cite: 9].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** Four 2D boundary markers on a field plot (`[0, 0]`, `[1, 0]`, `[1, 1]`, `[0, 1]` in scaled plot units) are rotated by `30°` and scaled by `1.5` along x and `2.0` along y in a 2D map coordinate system. Transformations are assumed linear with no translation offset.
* **New Input Data:** `points` (4 corners), `angle = np.deg2rad(30)`, `scale = np.array([[1.5, 0.0], [0.0, 2.0]])`.
* **Program Output:**
  ```text
  Original points:
   [[0. 0.]
   [1. 0.]
   [1. 1.]
   [0. 1.]]
  Transformation matrix:
   [[ 1.29903811 -1.        ]
   [ 0.75        1.73205081]]
  Transformed points:
   [[ 0.          0.        ]
   [ 1.29903811  0.75      ]
   [ 0.29903811  2.48205081]
   [-1.          1.73205081]]
  Determinant: 3.0



# Task 6: Solution of Systems of Linear Equations
**Program File:** `pylib/Task_06_linear_systems.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Coefficient matrix `A = [[4.0, 2.0], [8.0, 12.0]]` (CPU and memory per server type) and right-hand vector `b = [20.0, 72.0]` (total observed usage)[cite: 9]. Solves $Ax = b$ using `np.linalg.solve(A, b)` and checks the residual $r = b - Ax$ and Euclidean norm $\Vert{}r\Vert{}_2$[cite: 9, 10].
* **Parameter Change & Effect (C):** Changing total usage `b` from `[20.0, 72.0]` to `[24.0, 80.0]`[cite: 9] shifts the solution from `(3, 4)` to `(4, 4)` (4 Type A servers and 4 Type B servers) while keeping the residual norm near `0`.
* **Output & Graph Interpretation (D):** Prints `Type A servers: 3` and `Type B servers: 4`, verifies `A @ solution` equals `[20., 72.]`, and shows a near-zero residual norm confirming exact accuracy[cite: 9, 10]. No graph is generated[cite: 9, 10].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A network team allocates two container profiles (Worker and Database) that consume fixed bandwidth (Gbps) and SSD storage (GB), assuming exact resource totals with no idle overhead.
* **New Input Data:** `A = np.array([[3.0, 5.0], [50.0, 120.0]])` and `b = np.array([31.0, 660.0])`.
* **Program Output:**
  ```text
  Worker containers: 2
  Database containers: 5
  Verification A @ solution: [ 31. 660.]
  Residual: [0. 0.]
  Residual norm: 0.0


# Task 7: Gaussian Elimination and LU Decomposition
**Program File:** `pylib/Task_07_gaussian_lu.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Fixed $3 \times 3$ coefficient matrix `A` and three right-hand `measurement_sets` vectors `b`[cite: 11]. Factors $PA = LU$ once using `scipy.linalg.lu_factor(A)`, then solves all three systems using `lu_solve((lu, piv), b)` and verifies the residual norm[cite: 11, 12].
* **Parameter Change & Effect (C):** Changing the diagonal entries of `A` from `[4.0, 4.0, 3.0]` to `[5.0, 5.0, 4.0]`[cite: 11] reduces the magnitude of every element in the solution vector `x` because larger diagonal weights require smaller variable values for the same `b` vectors.
* **Output & Graph Interpretation (D):** Prints the 3-element solution vector and a residual norm near `10^-15` for each measurement set, and confirms `lu_solve` matches `np.linalg.solve` directly[cite: 12]. No graph is generated[cite: 11, 12].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A manufacturing line reuses the same 3-station machine coupling matrix `A` across three daily shifts while target demand vectors `b` vary per shift; system parameters are assumed linear and constant across shifts.
* **New Input Data:** `A` (same $3 \times 3$ matrix) and three shift demand vectors `[18.0, 12.0, 11.0]`, `[20.0, 15.0, 10.0]`, and `[14.0, 10.0, 9.0]`.
* **Program Output:**
  ```text
  Measurement set 1
  Solution: [5.725 4.9   5.3  ]
  Residual norm: 0.0

  Measurement set 2
  Solution: [6.575 6.3   5.43333333]
  Residual norm: 1.7763568394002505e-15

  Measurement set 3
  Solution: [4.625 4.5   4.5  ]
  Residual norm: 0.0

  Direct solution for first set: [5.725 4.9   5.3  ]


# Task 8: Iterative Methods for Linear Systems
**Program File:** `pylib/Task_08_iterative_linear.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** $5 \times 5$ diagonally dominant matrix `A`, boundary vector `b = [100., 0., 0., 0., 20.]`, `tol=1e-8`, and `max_iter=500`[cite: 12, 13]. Runs Jacobi and Gauss-Seidel iterations, tracks infinity-norm step changes, and plots convergence via `plt.semilogy()`[cite: 13, 14].
* **Parameter Change & Effect (C):** Relaxing `tol` from `1e-8` to `1e-4`[cite: 13] reduces the number of iterations roughly by half while slightly lowering decimal accuracy in `x_j` and `x_gs`.
* **Output & Graph Interpretation (D):** Both methods converge to `[86.67, 73.33, 60.00, 46.67, 33.33]`, matching `Direct solution`[cite: 13]. On the semi-log graph, Gauss-Seidel's curve drops nearly twice as steeply as Jacobi's because it uses newly updated neighbor values immediately[cite: 13, 14].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** Five interior nodes along a steady-state DC resistive voltage bus sit between a `48 V` left supply and a `12 V` right load, modeled with uniform neighbor conductance (`2` on diagonal, `-1` off-diagonal).
* **New Input Data:** Same $5 \times 5$ matrix `A`, boundary vector `b = np.array([48., 0., 0., 0., 12.])`, `tol=1e-8`, `max_iter=500`.
* **Program Output:**
  ```text
  Jacobi voltages: [42. 36. 30. 24. 18.]
  Gauss-Seidel voltages: [42. 36. 30. 24. 18.]
  Direct solution: [42. 36. 30. 24. 18.]



# Task 9: Eigenvalues and Eigenvectors
**Program File:** `pylib/Task_09_eigenvalues.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** $4 \times 4$ binary symmetric adjacency matrix `A` for nodes `A, B, C, D`[cite: 14, 15]. Computes eigenvalues and eigenvectors using `np.linalg.eig(A)`, normalizes the dominant eigenvector to sum to `1.0`, and verifies $\Vert{}Av - \lambda v\Vert{}_2$[cite: 14, 15].
* **Parameter Change & Effect (C):** Connecting node `A` directly to node `D` (`A[0, 3] = 1.0`, `A[3, 0] = 1.0`)[cite: 14] makes all four nodes equally connected (degree 3), increasing the dominant eigenvalue from `2.5616` to `3.0` and equalizing all importance scores to `0.2500`.
* **Output & Graph Interpretation (D):** Nodes `B` and `C` get higher importance (`0.3049`) than `A` and `D` (`0.1951`) due to having more connections, and the near-zero verification error confirms $Av = \lambda v$[cite: 14, 15]. No graph is generated[cite: 14, 15].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** Four interconnected microservices (`Auth`, `Gateway`, `Orders`, `Billing`) have bidirectional API links represented as an unweighted undirected adjacency matrix (`1.0` = linked, `0.0` = unlinked).
* **New Input Data:** `nodes = ["Auth", "Gateway", "Orders", "Billing"]` and modified $4 \times 4$ adjacency matrix `A` where `Gateway` connects to all three other services.
* **Program Output:**
  ```text
  Dominant eigenvalue: 2.1701
  Eigenvector-based importance:
  Auth: 0.2464
  Gateway: 0.3822
  Orders: 0.1857
  Billing: 0.1857
  Verification error: 6.280369834735101e-16



 # Task 10: Root Finding: Bisection and Fixed-Point Methods
**Program File:** `pylib/Task_10_bisection_fixed_point.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Heat-balance function `heat_balance(T) = T - 25 - 10 * exp(-T / 20)` over bracket `[20, 40]`, tolerance `xtol=1e-10`, fixed-point iteration `g(T) = 25 + 10 * exp(-T / 20)` starting at `T = 30.0` (up to `100` steps), and plotting `heat_balance(temps)` across `20` to `40`[cite: 15, 16]. Uses `scipy.optimize.root_scalar(..., method="bisect")` and fixed-point updates[cite: 15, 16].
* **Parameter Change & Effect (C):** Changing the initial guess `T` in fixed-point iteration from `30.0` to `20.0`[cite: 16] changes the step-by-step trajectory and iteration count slightly, but converges to the exact same equilibrium root because `g'(T)` is contractive near the solution.
* **Output & Graph Interpretation (D):** Prints the bisection root, fixed-point equilibrium value, and iteration count, matching to six decimal places[cite: 16]. The plot shows the curve crossing zero (`y = 0`) at the dashed vertical line marking the equilibrium temperature[cite: 16].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A water-tank thermal model balances heat gain and heat loss around an equilibrium temperature `T` (°C), with a constant ambient offset and exponential loss term over `[15, 35]`.
* **New Input Data:** `def heat_balance(T): return T - 20 - 8 * np.exp(-T / 18)`, bracket `[15, 35]`, `xtol=1e-10`, `g(T) = 20 + 8 * np.exp(-T / 18)`, starting guess `T = 25.0`.
* **Program Output:**
  ```text
  Bisection equilibrium temperature: 21.855143 C
  Fixed-point equilibrium temperature: 21.855143 C
  Fixed-point iterations: 6


# Task 11: Root Finding: Newton-Raphson and Secant Methods
**Program File:** `pylib/Task_11_newton_secant.py`

### 1. Original Task Analysis (Parts B, C & D)
* **Inputs & Operations (B):** Cash flow list `cash_flows = [-10000, 3000, 3500, 4000, 2500]`, `npv(rate)` function, analytical derivative `d_npv(rate)`, initial guess `x0=0.10` for Newton's method, secant starting points `x0=0.05, x1=0.20`, and tolerance `xtol=1e-12`[cite: 17, 18]. Solves for the discount rate where `NPV(rate) = 0` via `scipy.optimize.root_scalar` using `"newton"` and `"secant"`[cite: 17, 18].
* **Parameter Change & Effect (C):** Increasing the final cash inflow (`cash_flows[4]`) from `2500` to `4000`[cite: 17] increases the internal rate of return (IRR) because total positive cash inflows are higher for the same `-10000` initial outlay.
* **Output & Graph Interpretation (D):** Prints the IRR from Newton-Raphson and the Secant method along with `NPV(newton.root)` near `0.0`[cite: 17, 18]. No graph is generated[cite: 17, 18].

### 2. Modified Real-World Case (Part E)
* **New Scenario & Assumptions:** A small project requires an initial capital outlay followed by four annual net cash inflows; cash flows occur at exact annual intervals and the discount rate is constant across periods.
* **New Input Data:** `cash_flows = [-12000, 3500, 4000, 4200, 3000]`, Newton starting guess `x0=0.10`, secant points `x0=0.05, x1=0.20`, `xtol=1e-12`.
* **Program Output:**
  ```text
  IRR using Newton-Raphson: 7.454784%
  IRR using Secant method: 7.454784%
  NPV at Newton solution: -0.000000



  