import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # backtrack
        res = []
        counter = Counter(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])

            for n in counter:
                if counter[n] == 0:
                    continue
                counter[n] -= 1
                cur.append(n)
                backtrack(cur)
                cur.pop()
                counter[n] += 1

        backtrack([])
        return res

    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        def sub(nums):
            if not nums:
                return {(), }

            res = set()
            for i, n in enumerate(nums):
                for perm in sub(nums[:i]+nums[i+1:]):
                    res.add((n,)+perm)
            return res

        return list(list(num) for num in sub(nums))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 2]
        expected = [
            [1, 1, 2],
            [1, 2, 1],
            [2, 1, 1]
        ]
        self.assertCountEqual(sol.permuteUnique(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
