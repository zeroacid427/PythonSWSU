import unittest
import math

def compute_result(x):
    if x < 0.2:
        y = math.sin(x)**2 + math.cos(x**2)
    else:
        y = math.cos(x) + math.exp(math.sqrt(x**2 + 0.1))
    return y

class TestComputeResult(unittest.TestCase):
    def test_compute_result(self):
        # Тест для значения x < 0.2
        x = 0.1
        expected_result = math.sin(x)**2 + math.cos(x**2)
        self.assertAlmostEqual(compute_result(x), expected_result)

        # Тест для значения x >= 0.2
        x = 0.5
        expected_result = math.cos(x) + math.exp(math.sqrt(x**2 + 0.1))
        self.assertAlmostEqual(compute_result(x), expected_result)

if __name__ == '__main__':
    unittest.main()
