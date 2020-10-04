import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def minDistance2(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        if not (N and M):
            return N or M
        dp = [[0]*M for _ in range(N)]

        # init first row
        for i in range(M):
            if word2[i] == word1[0]:
                dp[0][i] = dp[0][i-1] if i >= 1 else 0
            else:
                dp[0][i] = 1 + (dp[0][i-1] if i >= 1 else 0)

        for i in range(1, N):
            ch1 = word1[i]
            for j in range(M):
                ch2 = word2[j]
                if ch1 == ch2:
                    dp[i][j] = dp[i-1][j-1] if j >= 1 else i
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1] if j >= 1 else math.inf,
                                       dp[i][j-1] if j >= 1 else math.inf,
                                       dp[i-1][j])

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        if not (N and M):
            return N or M
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(M+1):
            dp[0][i] = i
        for i in range(N+1):
            dp[i][0] = i

        for i in range(1, N+1):
            ch1 = word1[i-1]
            for j in range(1, M+1):
                ch2 = word2[j-1]
                if ch1 == ch2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],
                                       dp[i][j-1],
                                       dp[i-1][j])

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

    def test_case_3(self):
        sol = Solution()
        word1 = "cb"
        word2 = ""
        expected = 2
        self.assertEqual(sol.minDistance(word1, word2), expected)

    def test_case_4(self):
        sol = Solution()
        word1 = "pneumonoultramicroscopicsilicovolcanoconiosis"
        word2 = "ultramicroscopically"
        expected = 27
        self.assertEqual(sol.minDistance(word1, word2), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
