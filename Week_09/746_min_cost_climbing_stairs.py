import unittest
from typing import List
from pprint import pprint


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1, f2 = 0, 0
        for i in range(2, len(cost)+1):
            f1, f2 = f2, min(cost[i-1]+f2, cost[i-2]+f1)
        return f2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        cost = [10, 15, 20]
        expected = 15
        self.assertEqual(sol.minCostClimbingStairs(cost), expected)

    def test_case_2(self):
        sol = Solution()
        cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        expected = 6
        self.assertEqual(sol.minCostClimbingStairs(cost), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
