import unittest
from typing import List
from pprint import pprint


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n-1) == 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        res = True
        self.assertEqual(sol.isPowerOfTwo(n), res)

    def test_case_2(self):
        sol = Solution()
        n = 16
        res = True
        self.assertEqual(sol.isPowerOfTwo(n), res)

    def test_case_3(self):
        sol = Solution()
        n = 3
        res = False
        self.assertEqual(sol.isPowerOfTwo(n), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
