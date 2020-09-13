import unittest
from typing import List
from pprint import pprint


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        cache = set()

        def sub(nums, head):
            if head in cache:
                return
            if not nums:
                return [[]]
            res = []
            for i, n in enumerate(nums):
                sub_res = sub(nums[:i]+nums[i+1:], head+(n,))
                if sub_res is None:
                    continue
                for r in sub_res:
                    r.append(n)
                    res.append(r)
            cache.add(head)
            return res

        return sub(nums, ())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 2]
        print(sol.permuteUnique(nums))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
