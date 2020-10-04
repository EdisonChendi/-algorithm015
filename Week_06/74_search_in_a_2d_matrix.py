import unittest
from typing import List
from pprint import pprint
import bisect


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        first_col = [row[0] for row in matrix]
        row_idx = bisect.bisect_right(first_col, target)
        row = matrix[row_idx-1]
        if row[0] == target:
            return True

        col_idx = bisect.bisect_right(row, target)
        if row[col_idx-1] == target:
            return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        H, W = len(matrix), len(matrix[0])
        l, r = 0, H*W-1
        while l <= r:
            mid = (r+l)//2
            row, col = divmod(mid, W)
            mid_v = matrix[row][col]
            if mid_v == target:
                return True
            if mid_v > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 13
        expected = False
        self.assertEqual(sol.searchMatrix(matrix, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
