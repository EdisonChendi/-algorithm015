import unittest
from typing import List
from pprint import pprint


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        # snow ball
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        for j in range(i+1, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 标准解法
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [0, 1, 0, 3, 12]
        expected = [1, 3, 12, 0, 0]
        sol.moveZeroes(nums)
        self.assertListEqual(nums, expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
