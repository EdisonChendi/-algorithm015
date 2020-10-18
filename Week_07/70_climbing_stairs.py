import unittest
from typing import List
from pprint import pprint


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f1, f2 = 1, 2
        for i in range(2, n+1):
            f1, f2 = f2, f1+f2
        return f2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
