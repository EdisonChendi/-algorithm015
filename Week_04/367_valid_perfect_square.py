import unittest
from typing import List
from pprint import pprint


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in {1, 4}:
            return True
        if num == 3:
            return False
        left, right = 2, num // 2
        while left <= right:
            n = left + (right-left) // 2
            if n*n == num:
                return True
            if n*n > num:
                right = n - 1
            else:
                left = n + 1
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        num = 16
        expected = True
        self.assertEqual(sol.isPerfectSquare(num), expected)

    def test_case_2(self):
        sol = Solution()
        num = 14
        expected = False
        self.assertEqual(sol.isPerfectSquare(num), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
