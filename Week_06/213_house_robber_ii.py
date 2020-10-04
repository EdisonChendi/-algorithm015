import unittest
from typing import List
from pprint import pprint


class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub(nums):
            y, n = 0, 0
            for money in nums:
                y, n = n+money, max(y, n)
            return max(y, n)

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(sub(nums[1:]), sub(nums[:-1]))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 2]
        expected = 3
        self.assertEqual(sol.rob(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        self.assertEqual(sol.rob(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
