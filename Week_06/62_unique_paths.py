import unittest
from typing import List
from pprint import pprint


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[1]*(n) for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        m = 3
        n = 7
        expected = 28
        self.assertEqual(sol.uniquePaths(m, n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
