import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def relativeSortArray1(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        res = []
        for n in arr2:
            res.extend([n, ]*counter.pop(n))
        for n in sorted(counter.keys()):
            res.extend([n, ]*counter[n])
        return res

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda a: order.get(a, a+1001))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
        arr2 = [2, 1, 4, 3, 9, 6]
        expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
        self.assertListEqual(sol.relativeSortArray(arr1, arr2), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
