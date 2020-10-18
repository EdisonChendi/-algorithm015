import unittest
from typing import List
from pprint import pprint


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            row = rows[i]
            for j in range(9):
                ch = board[i][j]

                if ch == ".":
                    continue

                col = cols[j]
                box = boxes[i//3*3+j//3]
                if ch in row or ch in col or ch in box:
                    return False
                row.add(ch)
                col.add(ch)
                box.add(ch)

        return True


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
