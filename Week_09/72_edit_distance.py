import unittest
from typing import List
from pprint import pprint


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] = dp[i-1][j-1] if w[i] == w[j]
        # dp[i][j] = 1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) if w[i] != w[j]
        N1, N2 = len(word1), len(word2)
        if N1 * N2 == 0:
            return N1 or N2

        dp = [[0, ]*(N1+1) for _ in range(N2+1)]
        dp[0][0] = 0
        for i in range(1, N1+1):
            dp[0][i] = i
        for i in range(1, N2+1):
            dp[i][0] = i
        for i in range(1, N2+1):
            for j in range(1, N1+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

        return dp[-1][-1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        word1 = "horse"
        word2 = "ros"
        expected = 3
        self.assertEqual(sol.minDistance(word1, word2), expected)

    def test_case_2(self):
        sol = Solution()
        word1 = "intention"
        word2 = "execution"
        expected = 5
        self.assertEqual(sol.minDistance(word1, word2), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
