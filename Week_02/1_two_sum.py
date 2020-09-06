import unittest
from typing import List
from pprint import pprint


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target-n in seen:
                return [seen[target-n], i]
            seen[n] = i
        return []


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertListEqual(sol.twoSum(nums, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
