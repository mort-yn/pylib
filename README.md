## Task 2: NumPy Arrays and Numerical Computation
**Program File:** `code/Task_02_numpy_arrays.py`

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

  ## Task 3: Mathematical Functions and Vectorization
**Program File:** `code/Task_03_vectorization.py`

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

  ## Task 4: Floating-Point Arithmetic and Numerical Errors
**Program File:** `code/Task_04_numerical_errors.py`

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


  ## Task 5: Matrix Algebra and Matrix Operations
**Program File:** `code/Task_05_matrix_algebra.py`

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

  