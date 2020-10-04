import unittest
from typing import List
from pprint import pprint


class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        # optimal substructure
        # without after effect
        # overlapping subproblems
        # dp[i][j] = 1+dp[i-1][j-1] if t1[i] == t2[j] else max(dp[i][j-1], dp[i-1][j])
        L1, L2 = len(text1), len(text2)
        dp = [[0] * (L2+1) for _ in range(L1+1)]
        for i in range(1, L1+1):
            for j in range(1, L2+1):
                ch1, ch2 = text1[i-1], text2[j-1]
                dp[i][j] = (1 + dp[i-1][j-1]
                            ) if ch1 == ch2 else max(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top-down
        cache = {}

        def sub(text1, text2):
            if not text1 or not text2:
                return 0
            if (text1, text2) in cache:
                return cache[(text1, text2)]
            if (text2, text1) in cache:
                return cache[(text2, text1)]

            if text1[-1] == text2[-1]:
                res = 1 + sub(text1[:-1], text2[:-1])
            else:
                res = max(sub(text1, text2[:-1]), sub(text1[:-1], text2))

            cache[(text1, text2)] = res
            return res

        return sub(text1, text2)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_case_2(self):
        sol = Solution()
        text1 = "abc"
        text2 = "abc"
        expected = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_case_3(self):
        sol = Solution()
        text1 = "abc"
        text2 = "def"
        expected = 0
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    def test_case_4(self):
        sol = Solution()
        text1 = "ylqpejqbalahwr"
        text2 = "yrkzavgdmdgtqpg"
        expected = 3
        self.assertEqual(sol.longestCommonSubsequence(text1, text2), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
