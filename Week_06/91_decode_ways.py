import unittest
from typing import List
from pprint import pprint


class Solution:
    def numDecodings(self, s: str) -> int:
        # optimal substructure
        # without after effect
        # overlapping subproblems
        if not s:
            return 0

        N = len(s)
        if s[0] == '0':
            return 0

        dp2, dp1 = 1, 1
        for cur, last in zip(s[1:], s):
            if cur == '0':
                if last not in {'1', '2'}:
                    return 0
                dp = dp2
            else:
                # cur != '0'
                dp = dp1
                if last != '0' and 0 <= int(last+cur) <= 26:
                    dp += dp2
            dp2, dp1 = dp1, dp
        return dp1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "12"
        expected = 2
        self.assertEqual(sol.numDecodings(s), expected)

    def test_case_2(self):
        sol = Solution()
        s = "226"
        expected = 3
        self.assertEqual(sol.numDecodings(s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
