# Case Study — Stock Coverage (Days of Supply)

> ⚠️ **100% synthetic data.** None of the data in this project comes from any real
> company. Everything is generated randomly by `generate_synthetic_data.py`. This project
> illustrates an analysis **methodology**, not a specific business case.

## What it's about

Stock coverage answers: **how many days will current inventory last, at the rate it's
being consumed?**

Coverage = Current stock ÷ Average daily consumption

The project shows that the key methodological decision is not the alert threshold, but the
**consumption window** used to estimate demand.

## How to set it up in VS Code (one time)

1. Open this folder in VS Code (`File > Open Folder`).
2. Open an integrated terminal (`Terminal > New Terminal`).
3. Install the libraries:
   ```
   pip install pandas numpy matplotlib jupyter
   ```
4. Install the Microsoft **Python** and **Jupyter** extensions (Extensions sidebar,
   search "Python" and "Jupyter").
5. Generate the data:
   ```
   python generate_synthetic_data.py
   ```
   This creates the three CSV files inside `data/`.

## Files

- `generate_synthetic_data.py` — generates the synthetic data (already done).
- `data/` — the generated CSVs: products, daily consumption, current inventory.
- `analysis.py` — **this is where you write the analysis**, block by block.

## Progress

- [x] Synthetic data generated
- [ ] Block 1 — load and explore the data
- [ ] Block 2 — compute average daily consumption
- [ ] Block 3 — compute days of coverage
- [ ] Block 4 — the fixed-threshold problem
- [ ] Block 5 — visualization
- [ ] Block 6 — conclusion and publishing
