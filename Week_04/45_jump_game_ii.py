import unittest
from typing import List
from pprint import pprint


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        count = 0
        N = len(nums)
        window = [0, 1]
        max_jump = -1
        while True:
            max_jump = -1
            count += 1
            for i in range(window[0], window[1]):
                max_jump = max(max_jump, i+nums[i])
            if max_jump >= N-1:
                return count
            window = [window[1], max_jump+1]


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 3, 1, 1, 4]
        expected = 2
        self.assertEqual(sol.jump(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2]
        expected = 0
        self.assertEqual(sol.jump(nums), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
