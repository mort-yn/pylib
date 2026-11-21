import matplotlib.pyplot as plt
import numpy as np

# Flow sensor samples: time in seconds and cumulative volume in litres
time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
volume = np.array([0.0, 2.5, 5.4, 8.7, 12.4, 16.5, 21.0])

flow_rate = np.zeros_like(volume)

# Forward difference at the beginning
flow_rate[0] = (volume[1] - volume[0]) / (time[1] - time[0])

# Central differences for interior points
for i in range(1, len(time) - 1):
    flow_rate[i] = (volume[i + 1] - volume[i - 1]) / (time[i + 1] - time[i - 1])

# Backward difference at the end
flow_rate[-1] = (volume[-1] - volume[-2]) / (time[-1] - time[-2])

for t, v, q in zip(time, volume, flow_rate):
    print(f"t={t:.0f}s, volume={v:.1f}L, estimated flow={q:.2f} L/s")

plt.plot(time, flow_rate, marker="o")
plt.xlabel("Time (s)")
plt.ylabel("Estimated flow rate (L/s)")
plt.title("Flow rate estimated from cumulative volume data")
plt.grid(True)
plt.show()