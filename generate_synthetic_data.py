"""
generate_synthetic_data.py
---------------------------
Generates COMPLETELY SYNTHETIC inventory and consumption data for the
Stock Coverage (Days of Supply) case study.

None of this data comes from any real company. All SKUs, quantities and
dates are generated randomly and deterministically (fixed seed) so the
study is reproducible.

Usage:  python generate_synthetic_data.py
"""

import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)  # fixed seed -> reproducible results

# ---------------------------------------------------------------
# 1. Fictional product catalog
# ---------------------------------------------------------------
N_SKUS = 40
categories = ["Electronics", "Home", "Sports", "Office", "Garden"]

skus = pd.DataFrame({
    "sku_id": [f"SKU-{i:04d}" for i in range(1, N_SKUS + 1)],
    "category": RNG.choice(categories, N_SKUS),
    # "base" turnover: average units consumed per day for that product
    "base_daily_consumption": RNG.uniform(0.5, 25, N_SKUS).round(2),
})

# ---------------------------------------------------------------
# 2. Daily consumption time series (180 days)
# ---------------------------------------------------------------
dates = pd.date_range("2025-01-01", periods=180, freq="D")

rows = []
for _, s in skus.iterrows():
    base = s["base_daily_consumption"]
    seasonal = 1 + 0.3 * np.sin(np.linspace(0, 6 * np.pi, len(dates)))  # gentle waves
    noise = RNG.normal(1, 0.25, len(dates)).clip(0.1, None)            # daily variation
    spikes = RNG.choice([1, 1, 1, 1, 3], len(dates))                  # ~20% of days spike x3
    consumption = (base * seasonal * noise * spikes).round().astype(int).clip(0, None)
    for d, c in zip(dates, consumption):
        rows.append((s["sku_id"], d, c))

consumption_df = pd.DataFrame(rows, columns=["sku_id", "date", "units_consumed"])

# ---------------------------------------------------------------
# 3. Current inventory level (snapshot at cutoff date)
# ---------------------------------------------------------------
cutoff_date = dates[-1]
inventory_df = pd.DataFrame({
    "sku_id": skus["sku_id"],
    "cutoff_date": cutoff_date,
    "current_stock": RNG.integers(0, 1200, N_SKUS),
})

# ---------------------------------------------------------------
# 4. Save to CSV
# ---------------------------------------------------------------
skus.to_csv("data/products.csv", index=False)
consumption_df.to_csv("data/daily_consumption.csv", index=False)
inventory_df.to_csv("data/current_inventory.csv", index=False)

print("Synthetic data generated:")
print(f"  data/products.csv           -> {len(skus)} rows")
print(f"  data/daily_consumption.csv  -> {len(consumption_df)} rows")
print(f"  data/current_inventory.csv  -> {len(inventory_df)} rows")
print(f"  Cutoff date: {cutoff_date.date()}")
