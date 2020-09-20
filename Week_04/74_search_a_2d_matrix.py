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
        if row_idx == 0:
            return False

        search_row = matrix[row_idx-1]
        if search_row[0] == target:
            return True

        col_idx = bisect.bisect_right(search_row, target)
        return col_idx > 0 and search_row[col_idx-1] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        H, W = len(matrix), len(matrix[0])
        left, right = 0, H*W-1
        while left <= right:
            mid = left + (right-left) // 2
            r, c = mid//W, mid % W
            v = matrix[r][c]
            if v == target:
                return True
            if v < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        target = 3
        expected = True
        self.assertEqual(sol.searchMatrix(matrix, target), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     matrix = [
    #         [1,   3,  5,  7],
    #         [10, 11, 16, 20],
    #         [23, 30, 34, 50]
    #     ]
    #     target = 13
    #     expected = False
    #     self.assertEqual(sol.searchMatrix(matrix, target), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
