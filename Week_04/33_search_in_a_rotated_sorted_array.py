import unittest
from typing import List
from pprint import pprint
import bisect


def binary_search(nums, target, lo, hi):
    pos = bisect.bisect_left(nums, target, lo, hi)
    if pos == len(nums):
        return -1
    if target != nums[pos]:
        return -1
    else:
        return pos


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def sub(nums, target, lo, hi):
            if lo > hi:
                return -1

            mid = (lo+hi) // 2
            # print(f"mid:{mid}, nums[mid]:{nums[mid]}")
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[lo]:
                if nums[lo] <= target < nums[mid]:
                    return sub(nums, target, lo, mid-1)
                else:
                    return sub(nums, target, mid+1, hi)
            else:
                if nums[mid] < target <= nums[hi]:
                    return sub(nums, target, mid+1, hi)
                else:
                    return sub(nums, target, lo, mid-1)

        return sub(nums, target, 0, len(nums)-1)


class TestSolution(unittest.TestCase):

    # def test_case_1(self):
    #     sol = Solution()
    #     nums = [4, 5, 6, 7, 0, 1, 2]
    #     target = 0
    #     expected = 4
    #     self.assertEqual(sol.search(nums, target), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     nums = [4, 5, 6, 7, 0, 1, 2]
    #     target = 3
    #     expected = -1
    #     self.assertEqual(sol.search(nums, target), expected)

    # def test_case_3(self):
    #     sol = Solution()
    #     nums = [1]
    #     target = 0
    #     expected = -1
    #     self.assertEqual(sol.search(nums, target), expected)

    # def test_case_4(self):
    #     sol = Solution()
    #     nums = [1, 3]
    #     target = 2
    #     expected = -1
    #     self.assertEqual(sol.search(nums, target), expected)

    def test_case_5(self):
        sol = Solution()
        nums = [3, 1]
        target = 1
        expected = 1
        self.assertEqual(sol.search(nums, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
