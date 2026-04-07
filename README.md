# Statistical Engine & LLN Simulation

## Project Overview
This project implements a pure-Python statistical engine from scratch without using third-party data science libraries like NumPy or Pandas. It can process 1-dimensional numerical data to calculate central tendencies, measures of dispersion, and detect outliers. Additionally, it features a Monte Carlo simulation demonstrating the **Law of Large Numbers (LLN)** by repeatedly sampling an extreme startup salary dataset.

## Mathematical Logic

### Median (Even vs. Odd)
To calculate the median accurately, the dataset is first sorted. 
- If the number of data points (n) is **odd**, the median is simply the middle value at index `n // 2`.
- If the number of data points (n) is **even**, no single middle value exists. Instead, the median is calculated as the arithmetic average of the two central values at indices `(n // 2) - 1` and `n // 2`.

### Variance & Bessel's Correction
The engine calculates both Population and Sample Variance based on the `is_sample` flag.
- **Population Variance ($\sigma^2$)**: Calculated by finding the sum of squared differences from the mean, divided by the total number of data points ($n$). Use this when your data represents the entire population.
- **Sample Variance ($s^2$)**: Calculated similarly, but divided by $n - 1$ instead of $n$. This uses **Bessel's correction** to correct the downward bias that occurs when estimating population variance from a sample, ensuring a more accurate and unbiased estimate.

## Setup Instructions
1. **Navigate to the project directory:**
   Ensure you are in `c:\Users\asus\Documents\Projects\StatisticalFoundations-Simulations\statistical_engine`
2. **Run the main application:**
   The project requires no external libraries (uses only standard Python). Run the main script with:
   ```bash
   python main.py
   ```

## Testing
This project uses Python's built-in `unittest` framework to validate all statistical algorithms and edge-case handling.
- To execute the full test suite, run the following command from the project root:
  ```bash
  python -m unittest discover tests
  ```

## Acceptance Criteria Checklist
- [x] **Passes empty list handling:** Raises `ValueError` explicitly when encountering empty arrays after cleaning prevents `ZeroDivisionError`.
- [x] **Graceful Error Handling:** Cleans out purely `None` values and dynamically parses string-castable numerics; raises `TypeError` for genuinely un-castable data.
- [x] **Correct Mean/Median (Even vs Odd):** Implements correct median calculation for both even-length and odd-length datasets.
- [x] **Accurately calculates Sample Variance vs Population Variance:** Uses Bessel's Correction ($n-1$) intelligently depending on the requested context.
- [x] **Multimodal Mode Support:** `get_mode()` returns all modes if multimodal; correctly indicates if all elements are strictly unique.
- [x] **Outlier Detection:** Highlights data points more than N standard deviations from the underlying mean.
- [x] **LLN Simulation:** Shows empirical proof via randomized subsets iteratively scaling to approximate the real pop-parameters.
