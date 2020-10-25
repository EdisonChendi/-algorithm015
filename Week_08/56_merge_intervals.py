import unittest
from typing import List
from pprint import pprint


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) <= 1:
            return intervals

        intervals.sort()
        res = []
        merging = intervals[0]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= merging[1]:
                merging[1] = max(merging[1], cur[1])
            else:
                res.append(merging)
                merging = cur
        res.append(merging)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertListEqual(sol.merge(intervals), expected)

    def test_case_2(self):
        sol = Solution()
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertListEqual(sol.merge(intervals), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
