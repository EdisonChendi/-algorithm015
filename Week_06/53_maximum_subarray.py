import unittest
from typing import List
from pprint import pprint


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        last, m = nums[0], nums[0]
        for i in range(1, len(nums)):
            a, b = nums[i], nums[i] + last
            last = a if a > b else b
            m = max(m, last)
        return m


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        self.assertEqual(sol.maxSubArray(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
