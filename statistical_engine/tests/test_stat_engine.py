import sys
import os
import unittest

# Add parent directory to sys.path so that 'src' module can be discovered
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):
    def test_mean(self):
        engine = StatEngine([1, 2, 3, 4, 5])
        self.assertEqual(engine.get_mean(), 3.0)

    def test_median_odd_vs_even(self):
        engine_odd = StatEngine([1, 3, 5])
        self.assertEqual(engine_odd.get_median(), 3.0)
        
        engine_even = StatEngine([1, 3, 5, 7])
        self.assertEqual(engine_even.get_median(), 4.0)
        
    def test_mode(self):
        engine_unique = StatEngine([1, 2, 3])
        self.assertEqual(engine_unique.get_mode(), "No mode: all values are unique.")
        
        engine_multi = StatEngine([1, 1, 2, 2, 3])
        self.assertCountEqual(engine_multi.get_mode(), [1.0, 2.0])

    def test_empty_list_handling(self):
        with self.assertRaises(ValueError):
            StatEngine([])
            
    def test_data_cleaning_and_type_error(self):
        engine = StatEngine([1, '2', 3.0, None])
        self.assertEqual(engine.get_mean(), 2.0)
        
        with self.assertRaises(TypeError):
            StatEngine([1, 'abc', 3])

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=True), 2.138089935299395)
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), 2.0)
        
    def test_outliers(self):
        engine = StatEngine([10, 10, 10, 10, 10, 100])
        outliers = engine.get_outliers(threshold=1.5)
        self.assertIn(100.0, outliers)

if __name__ == '__main__':
    unittest.main()
