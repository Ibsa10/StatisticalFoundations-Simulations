class StatEngine:
    def __init__(self, data: list):
        # 1. Clean the data (remove None, ensure floats)
        self.data = []
        for x in data:
            if x is not None:
                try:
                    self.data.append(float(x))
                except (ValueError, TypeError):
                    raise TypeError(f"Cannot convert {x} to a number.")
                    
        # 2. Check if we have data left
        if len(self.data) == 0:
            raise ValueError("Dataset is empty.")

    def get_mean(self) -> float:
        # Sum of all elements divided by total count
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        # Sort data to find the middle
        data = sorted(self.data)
        n = len(data)
        mid = n // 2
        
        # Check if the number of elements is even or odd
        if n % 2 == 0:
            # Average of the two middle elements
            return (data[mid - 1] + data[mid]) / 2.0
        else:
            # The exact middle element
            return data[mid]

    def get_mode(self):
        # Count occurrences of each number
        freqs = {}
        for x in self.data:
            freqs[x] = freqs.get(x, 0) + 1
            
        max_freq = max(freqs.values())
        
        # Specific rule: if all numbers only appear once
        if max_freq == 1:
            return "No mode: all values are unique."
            
        # Build list of all numbers matching the highest frequency
        return [val for val, count in freqs.items() if count == max_freq]

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        if is_sample and n < 2:
            raise ValueError("Sample variance needs at least 2 data points.")
            
        mean = self.get_mean()
        
        # Calculate sum of squared differences from the mean
        sq_diffs = sum((x - mean) ** 2 for x in self.data)
        
        # Use Bessel's correction (n - 1) if it's a sample, else just (n)
        denominator = (n - 1) if is_sample else n
        return sq_diffs / denominator

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        # Math equivalent of square root is raising to the 0.5 power
        return self.get_variance(is_sample) ** 0.5

    def get_outliers(self, threshold: float = 2.0) -> list:
        # Avoid crashing if we can't calculate standard deviation
        if len(self.data) < 2:
            return []
            
        mean = self.get_mean()
        std_dev = self.get_standard_deviation(is_sample=True)
        
        # If there is no variation, there are no outliers
        if std_dev == 0:
            return []
            
        # Return points further away from the mean than (threshold * standard_deviation)
        return [x for x in self.data if abs(x - mean) > (threshold * std_dev)]
