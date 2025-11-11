# Exercise 1: Understanding the Importance of Testing

# Instruction:

# Write a small Python function (e.g., a function to calculate the square of a number) and intentionally introduce a bug (e.g., incorrect calculation logic).
# Exercise 2: Writing Basic Unit Tests

# Instruction:

# Use the unittest module in Python to create a test case for the buggy function from Exercise 1.
# Write test methods to check different scenarios (e.g., valid input, invalid input) and verify expected behavior.


import unittest

def square_of_number(x):
    
    return x ** 2


class TestSquare(unittest.TestCase):
    def test_square(self):
        result = square_of_number(6)
        self.assertEqual(result,36)
        
        
if __name__ == "__main__":
    unittest.main()