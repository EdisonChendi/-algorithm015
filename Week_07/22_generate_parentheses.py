import unittest
from typing import List
from pprint import pprint


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def sub(s, l, r, res):
            if l == 0 and r == 0:
                res.append(s)
                return

            if l > 0:
                sub(s+"(", l-1, r, res)
            if r > 0 and r > l:
                sub(s+")", l, r-1, res)
            return res

        return sub("", n, n, [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(sol.generateParenthesis(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
