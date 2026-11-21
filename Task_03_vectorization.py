import timeit
import numpy as np

rng = np.random.default_rng(101)
pixel_intensities = rng.integers(0, 256, size=1_000_000).astype(float)
gamma = 2.2


def loop_gamma():
    corrected = []
    for px in pixel_intensities:
        norm = px / 255.0
        corrected.append(norm ** gamma)
    return corrected


def vectorized_gamma():
    norm = pixel_intensities / 255.0
    return norm ** gamma


loop_time = timeit.timeit(loop_gamma, number=1)
vector_time = timeit.timeit(vectorized_gamma, number=3) / 3
result = vectorized_gamma()

print("First five gamma-corrected pixels:", np.round(result[:5], 6))
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")