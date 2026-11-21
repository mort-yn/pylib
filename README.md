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