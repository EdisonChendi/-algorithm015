import unittest
from typing import List
from pprint import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(board, r, cols, pies, nas, res):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for i in range(n):
                if i not in cols and r+i not in pies and r-i not in nas:
                    board[r][i] = "Q"
                    cols.add(i)
                    pies.add(r+i)
                    nas.add(r-i)
                    backtrack(board, r+1, cols, pies, nas, res)
                    board[r][i] = "."
                    cols.remove(i)
                    pies.remove(r+i)
                    nas.remove(r-i)

            return res

        if n == 0:
            return [[]]

        board = [["." for _ in range(n)] for _ in range(n)]
        return backtrack(board, 0, set(), set(), set(), [])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 1
        pprint(sol.solveNQueens(n))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
