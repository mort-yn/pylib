import numpy as np

# 12 bi-hourly soil moisture readings (%) over 24 hours
soil_moisture_pct = np.array([
    34.2, 33.0, 31.5, 29.8, 27.4, 24.9,
    23.1, 22.0, 36.5, 35.8, 35.0, 34.5
])

mean_moisture = np.mean(soil_moisture_pct)
min_moisture = np.min(soil_moisture_pct)
max_moisture = np.max(soil_moisture_pct)

# Vectorized conversion to fractional water content (0.0 to 1.0 scale)
moisture_fraction = soil_moisture_pct / 100.0
dry_readings = soil_moisture_pct[soil_moisture_pct < 25.0]

print(f"Mean soil moisture: {mean_moisture:.2f}%")
print(f"Minimum soil moisture: {min_moisture:.2f}%")
print(f"Maximum soil moisture: {max_moisture:.2f}%")
print("Moisture as fractions (first 6):", moisture_fraction[:6])
print("Dry-stress readings (<25%):", dry_readings)