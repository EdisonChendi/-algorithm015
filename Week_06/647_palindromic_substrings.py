import unittest
from typing import List
from pprint import pprint
from collections import defaultdict


class Solution:
    def countSubstrings(self, s: str) -> int:
        N, count, seen = len(s), 0, defaultdict(set)
        dp = [[0]*N for _ in range(N)]
        for i, ch in enumerate(s):
            for j in seen[ch]:
                if i-j == 1 or dp[j+1][i-1] == 1:
                    dp[j][i] = 1
                    count += 1
            seen[ch].add(i)
            dp[i][i] = 1
            count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "aaa"
        expected = 6
        self.assertEqual(sol.countSubstrings(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "abc"
        expected = 3
        self.assertEqual(sol.countSubstrings(s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
