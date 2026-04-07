import random
import sys
import os

# Allow direct execution by adding parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from .stat_engine import StatEngine
except ImportError:
    from stat_engine import StatEngine

def run_lln_simulation(data: list, max_sample_size: int, step: int = 10):
    """
    Simulates the Law of Large Numbers (LLN).
    Takes a dataset, finds the real population mean, then draws random 
    samples of steadily increasing sizes to watch the sample mean converge.
    """
    if not data:
        raise ValueError("Need data to run simulation.")
        
    pop_engine = StatEngine(data)
    
    results = {
        "population_mean": pop_engine.get_mean(),
        "sample_sizes": [],
        "sample_means": []
    }
    
    # range() generates sizes: 1, 11, 21, 31... up to max
    for size in range(1, max_sample_size + 1, step):
        # random.choices picks random elements allowing duplicates (sampling with replacement)
        sample = random.choices(data, k=size)
        
        # Get the mean of our new random sample
        sample_mean = StatEngine(sample).get_mean()
        
        # Save our progress
        results["sample_sizes"].append(size)
        results["sample_means"].append(sample_mean)
            
    return results

if __name__ == '__main__':
    # Add a quick demo so it can be run independently
    print("Running standalone Law of Large Numbers simulation...")
    sample_data = [random.randint(1, 100) for _ in range(1000)]
    results = run_lln_simulation(sample_data, max_sample_size=100, step=20)
    
    print(f"True Population Mean: {results['population_mean']:.2f}\n")
    print("Sample Size | Sample Mean")
    print("-" * 25)
    for size, mean in zip(results['sample_sizes'], results['sample_means']):
        print(f"{size:<11} | {mean:.2f}")
