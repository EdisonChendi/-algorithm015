import unittest
from typing import List
from pprint import pprint


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums or len(nums) <= 1:
            return nums
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        for _ in range(fast-slow-1):
            nums.pop()
        return slow + 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1]
        expected_nums = [1]
        expected_len = 1
        self.assertEqual(sol.removeDuplicates(nums), expected_len)
        self.assertListEqual(nums, expected_nums)

    def test_case_2(self):
        sol = Solution()
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_nums = [0, 1, 2, 3, 4]
        expected_len = 5
        res = sol.removeDuplicates(nums)
        self.assertEqual(res, expected_len)
        self.assertListEqual(nums, expected_nums)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
