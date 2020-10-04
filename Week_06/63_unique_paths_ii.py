import unittest
from typing import List
from pprint import pprint


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        H, W = len(obstacleGrid), len(obstacleGrid[0])
        o = obstacleGrid  # save some typing
        dp = [[0]*(W+1) for _ in range(H+1)]
        dp[0][1] = 1
        for i in range(1, H+1):
            for j in range(1, W+1):
                if o[i-1][j-1] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        o = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        expected = 2
        self.assertEqual(sol.uniquePathsWithObstacles(o), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
