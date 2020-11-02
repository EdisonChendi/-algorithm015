import unittest
from typing import List
from pprint import pprint


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] - LIS end at index i
        N = len(nums)
        if N <= 1:
            return N
        dp = [1]*N
        for i in range(1, N):
            dp[i] = 1+max([dp[j] for j in range(i) if nums[j] < nums[i]]+[0])
        return max(dp)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        self.assertEqual(sol.lengthOfLIS(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
