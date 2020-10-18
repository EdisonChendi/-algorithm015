import unittest
from typing import List
from pprint import pprint

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # step1: 预计算
        empties = []
        rows = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                for _ in range(9)]
        cols = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                for _ in range(9)]
        boxes = [{'1', '2', '3', '4', '5', '6', '7', '8', '9'}
                 for _ in range(9)]
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == '.':
                    empties.append((i, j))
                else:
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[i//3*3+j//3].remove(ch)

        # step2: backtrack
        def backtrack(i):
            if i == len(empties):
                return True

            r, c = empties[i]
            row, col, box = rows[r], cols[c], boxes[r//3*3+c//3]
            for ch in row & col & box:
                tmp = board[r][c]
                board[r][c] = ch
                row.remove(ch)
                col.remove(ch)
                box.remove(ch)
                if backtrack(i+1):
                    return True
                board[r][c] = tmp
                row.add(ch)
                col.add(ch)
                box.add(ch)
            return False

        backtrack(0)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                              ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        pprint(board)
        sol.solveSudoku(board)
        pprint(board)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
