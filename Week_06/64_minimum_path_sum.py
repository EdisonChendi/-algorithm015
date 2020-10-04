import unittest
from typing import List
from pprint import pprint

import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        W, H = len(grid[0]), len(grid)
        dp = [0] + [math.inf] * (W-1)
        for i in range(H):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, W):
                dp[j] = grid[i][j] + min(dp[j-1], dp[j])
        return dp[-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
        ]
        expected = 7
        self.assertEqual(sol.minPathSum(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
