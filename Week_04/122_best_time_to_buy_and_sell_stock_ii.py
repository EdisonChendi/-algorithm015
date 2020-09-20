import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum((p1 - p2) if p1 > p2 else 0 for p1, p2 in zip(prices[1:], prices))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        expected = 7
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_2(self):
        sol = Solution()
        prices = [1, 2, 3, 4, 5]
        expected = 4
        self.assertEqual(sol.maxProfit(prices), expected)

    def test_case_3(self):
        sol = Solution()
        prices = [1]
        expected = 0
        self.assertEqual(sol.maxProfit(prices), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
