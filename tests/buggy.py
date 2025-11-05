import unittest

def square_of_number(x):
    
    return x ** 2


class TestSquare(unittest.TestCase):
    def test_square(self):
        result = square_of_number(6)
        self.assertEqual(result,36)
        
        
if __name__ == "__main__":
    unittest.main()