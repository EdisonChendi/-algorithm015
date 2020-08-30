import unittest
from typing import List
from pprint import pprint
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # in-place
        # [4,3,2,1,7,6,5]
        # [5,6,7,1,2,3,4]
        def rev(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        k %= len(nums)
        rev(0, len(nums)-k-1)
        rev(len(nums)-k, len(nums)-1)
        rev(0, len(nums)-1)
        return nums

    def rotate3(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        s1, s2 = [], []
        for _ in range(k):
            s1.append(nums.pop())
        for _ in range(k):
            s2.append(s1.pop())
        return s2 + nums

    def rotate2(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        deq = deque()
        for _ in range(k):
            deq.appendleft(nums.pop())
        return list(deq) + nums

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        return nums[-k:]+nums[:len(nums)-k]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        self.assertListEqual(sol.rotate(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [-1, -100, 3, 99]
        k = 2
        expected = [3, 99, -1, -100]
        self.assertListEqual(sol.rotate(nums, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
