import json
import os
from src.stat_engine import StatEngine
from src.monte_carlo import run_lln_simulation

def main():
    print("=== Statistical Engine Initialization ===\n")
    
    # Load sample salaries
    data_path = os.path.join(os.path.dirname(__file__), "data", "sample_salaries.json")
    try:
        with open(data_path, "r") as f:
            salaries = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find data file at {data_path}")
        return

    # Initialize Engine
    engine = StatEngine(salaries)
    
    print("[ Descriptives ]")
    print(f"Mean Salary:   ${engine.get_mean():,.2f}")
    print(f"Median Salary: ${engine.get_median():,.2f}")
    
    mode_result = engine.get_mode()
    if isinstance(mode_result, str):
        print(f"Mode:          {mode_result}")
    else:
        print(f"Mode:          ${', $'.join(f'{m:,.2f}' for m in mode_result)}")

    print(f"\nPopulation Variance:      ${engine.get_variance(is_sample=False):,.2f}")
    print(f"Sample Variance:          ${engine.get_variance(is_sample=True):,.2f}")
    print(f"Population Std Deviation: ${engine.get_standard_deviation(is_sample=False):,.2f}")
    print(f"Sample Std Deviation:     ${engine.get_standard_deviation(is_sample=True):,.2f}")
    
    outliers = engine.get_outliers(threshold=2.0)
    print(f"\nOutliers (> 2 std devs from mean):")
    if outliers:
        for out in outliers:
            print(f" - ${out:,.2f}")
    else:
        print(" - None found")
        
    print("\n=== Law of Large Numbers (LLN) Simulation ===")
    print("Simulating sample means converging to the population mean...")
    
    # Run LLN simulation
    lln_results = run_lln_simulation(salaries, max_sample_size=1000, step=100)
    
    pop_mean = lln_results["population_mean"]
    print(f"\nTrue Population Mean: ${pop_mean:,.2f}\n")
    
    print(f"{'Sample Size':<15} | {'Sample Mean':<20} | {'Absolute Error':<15}")
    print("-" * 55)
    for size, s_mean in zip(lln_results["sample_sizes"], lln_results["sample_means"]):
        error = abs(s_mean - pop_mean)
        print(f"{size:<15} | ${s_mean:<19,.2f} | ${error:<15,.2f}")

    print("\nInterpretation:")
    print("As the sample size increases, notice how the Sample Mean generally gets")
    print("closer to the True Population Mean, and the Absolute Error decreases.")
    print("This is the essence of the Law of Large Numbers.")

if __name__ == "__main__":
    main()
