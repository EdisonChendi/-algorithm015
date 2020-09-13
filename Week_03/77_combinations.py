import unittest
from typing import List
from pprint import pprint


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(s, cur):
            if len(cur) == k:
                res.append(cur[:])
                return

            for i in range(s, n+1):
                cur.append(i)
                backtrack(i+1, cur)
                cur.pop()

        backtrack(1, [])
        return res

    def combine1(self, n: int, k: int) -> List[List[int]]:

        def sub(s, l):
            if l == 0:
                return [[]]
            res = []
            for i in range(s, n+1):
                res.extend(([i]+r) for r in sub(i+1, l-1))
            return res

        return sub(1, k)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        print(sol.combine(4, 1))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
