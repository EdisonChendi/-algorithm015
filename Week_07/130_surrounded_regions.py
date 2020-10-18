import unittest
from typing import List
from pprint import pprint


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if not (0 <= i < H and 0 <= j < W) or board[i][j] != "O":
                return

            board[i][j] = "Y"
            for di, dj in directions:
                dfs(i+di, j+dj)

        if not board or not board[0]:
            return
        H, W = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # run dfs on border nodes
        for i in range(H):
            if i == 0 or i == H-1:
                for j in range(W):
                    dfs(i, j)
            else:
                dfs(i, 0)
                dfs(i, W-1)

        # loop though do flipping
        for i in range(H):
            for j in range(W):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
