import unittest
from typing import List
from pprint import pprint


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # simple recursion
        if not nums:
            return [[]]
        res = []
        for i, n in enumerate(nums):
            for r in self.permute(nums[:i]+nums[i+1:]):
                r.append(n)
                res.append(r)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 2]
        print(sol.permute(nums))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
