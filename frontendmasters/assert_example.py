import unittest

def multiply(x, y):
    return x + y

class Testmultiply(unittest.TestCase):

    def test_multiply(self):
        test_x = 5
        test_y = 5
        self.assertEqual(multiply(test_x, test_y), test_y * test_x)

if __name__ == "__main__":
    unittest.main()
