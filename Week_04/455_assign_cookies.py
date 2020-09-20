import unittest
from typing import List
from pprint import pprint


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g: greedy
        # s: cookie size
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                i += 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        g = [1, 2, 3]
        s = [1, 1]
        expected = 1
        self.assertEqual(sol.findContentChildren(g, s), expected)

    def test_case_2(self):
        sol = Solution()
        g = [1, 2]
        s = [1, 2, 3]
        expected = 2
        self.assertEqual(sol.findContentChildren(g, s), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
