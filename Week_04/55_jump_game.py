import unittest
from typing import List
from pprint import pprint


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        target = N-1
        for i in reversed(range(N-1)):
            jump = nums[i]
            if i+jump >= target:
                target = i
        return target == 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = True
        self.assertEqual(sol.canJump(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [3, 2, 1, 0, 4]
        expected = False
        self.assertEqual(sol.canJump(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [0, 4]
        expected = False
        self.assertEqual(sol.canJump(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
