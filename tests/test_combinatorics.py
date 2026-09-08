import unittest
from src.combinatorics import factorial, permutations, combinations

class TestCombinatorics(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

        with self.assertRaises(ValueError):
            factorial(-1)

    def test_permutations(self):
        self.assertEqual(permutations(5, 3), 60)
        self.assertEqual(permutations(5, 0), 1)
        self.assertEqual(permutations(5, 5), 120)

        with self.assertRaises(ValueError):
            permutations(5, 6)

        with self.assertRaises(ValueError):
            permutations(-1, 2)

    def test_combinations(self):
        self.assertEqual(combinations(5, 3), 10)
        self.assertEqual(combinations(5, 0), 1)
        self.assertEqual(combinations(5, 5), 1)

        with self.assertRaises(ValueError):
            combinations(5, 6)

        with self.assertRaises(ValueError):
            combinations(5, -1)

if __name__ == '__main__':
    unittest.main()
