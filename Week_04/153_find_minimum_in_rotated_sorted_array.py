import unittest
from typing import List
from pprint import pprint


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_min(lo, hi):
            # print(lo, hi)
            if nums[lo] <= nums[hi]:
                return nums[lo]

            mid = lo + (hi-lo) // 2
            if nums[mid] <= nums[mid-1] and nums[mid] <= nums[mid+1]:
                return nums[mid]

            if nums[mid] >= nums[lo]:
                return find_min(mid+1, hi)
            else:
                return find_min(lo, mid-1)

        return find_min(0, len(nums)-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 4, 5, 1, 2]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [2, 1]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [2, 3, 4, 5, 1]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [3, 1, 2]
        expected = 1
        self.assertEqual(sol.findMin(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
