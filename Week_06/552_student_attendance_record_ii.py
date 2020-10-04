import unittest
from typing import List
from pprint import pprint

# 'A' - one quota
# 'L' - no more than two continuous
# 'P' - all good

# DP problem:
# optimal substructure
# without after effect
# overlapping subproblems

# status:
# i - 0 1 2 ... n
# 'A' quota - 0 or 1
# 'L' quota - 0 or 1 or 2, choose not 'L' -> 0

# dp[i][A_quota][L_quota]
# dp[i][0][0] = dp[i-1][0][1] - choose 'L'
# dp[i][0][1] = dp[i-1][0][2] - choose 'L'
# dp[i][0][2] = dp[i-1][1][2] - choose 'A'
#             + dp[i-1][1][1] - choose 'A'
#             + dp[i-1][1][0] - choose 'A'
#             + dp[i-1][0][2] - choose 'P'
#             + dp[i-1][0][1] - choose 'P'
#             + dp[i-1][0][0] - choose 'P'

# dp[i][1][0] = dp[i-1][1][1] - chooose 'L'
# dp[i][1][1] = dp[i-1][1][2] - choose 'L'
# dp[i][1][2] = dp[i-1][1][2] - choose 'P'
#             + dp[i-1][1][1] - choose 'P'
#             + dp[i-1][1][0] - choose 'P'


class Solution:
    def checkRecord(self, n: int) -> int:
        M = 10**9+7
        dp = [[0]*3 for _ in range(2)]
        dp[1][2] = 1
        for i in range(1, n+1):
            new_dp = [[0]*3 for _ in range(2)]
            new_dp[0][0] = dp[0][1]
            new_dp[0][1] = dp[0][2]
            new_dp[0][2] = (dp[1][2] + dp[1][1] + dp[1][0] +
                            dp[0][2] + dp[0][1] + dp[0][0]) % M

            new_dp[1][0] = dp[1][1]
            new_dp[1][1] = dp[1][2]
            new_dp[1][2] = (dp[1][2] + dp[1][1] + dp[1][0]) % M

            dp = new_dp

        res = sum(dp[0]) + sum(dp[1])
        return res % M


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 2
        expected = 8
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_2(self):
        sol = Solution()
        n = 1
        expected = 3
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 0
        expected = 1
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_3(self):
        sol = Solution()
        n = 0
        expected = 1
        self.assertEqual(sol.checkRecord(n), expected)

    def test_case_4(self):
        sol = Solution()
        n = 100000
        expected = 749184020
        self.assertEqual(sol.checkRecord(n), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
