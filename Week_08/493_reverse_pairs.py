import unittest
from typing import List
from pprint import pprint


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def count_reverse_pairs(n1, n2):
            # O(n1+n2)
            doubled_n2, count, i, j = [n*2 for n in n2], 0, 0, 0
            while i < len(n1) and j < len(doubled_n2):
                vi, vj = n1[i], doubled_n2[j]
                if vi <= vj:
                    i += 1
                else:
                    count += len(n1) - i
                    j += 1
            return count

        def merge(n1, n2):
            # O(n1+n2)
            res, i, j = [], 0, 0
            while i < len(n1) and j < len(n2):
                vi, vj = n1[i], n2[j]
                if vi < vj:
                    res.append(vi)
                    i += 1
                else:
                    res.append(vj)
                    j += 1
            else:
                res.extend(n1[i:] or n2[j:])
            return res

        def sub(nums):
            # O(NlgN)
            nonlocal count

            N = len(nums)
            if N == 1:
                return nums

            sl, sr = sub(nums[:N//2]), sub(nums[N//2:])
            count += count_reverse_pairs(sl, sr)  # O(N)
            return merge(sl, sr)  # O(N)

        if len(nums) <= 1:
            return 0

        count = 0
        sub(nums)
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 3, 2, 3, 1]
        expected = 2
        self.assertEqual(sol.reversePairs(nums), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [2, 4, 3, 5, 1]
        expected = 3
        self.assertEqual(sol.reversePairs(nums), expected)

    def test_case_3(self):
        sol = Solution()
        nums = [-5, -5]
        expected = 1
        self.assertEqual(sol.reversePairs(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
