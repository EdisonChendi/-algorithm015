import unittest
from typing import List
from pprint import pprint


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0),
                      (1, 1), (-1, -1), (1, -1), (-1, 1))
        width, height = len(board[0]), len(board)

        def valid_pos(i, j):
            return 0 <= i < height and 0 <= j < width

        def dfs(i, j):
            if board[i][j] == 'M':
                board[i][j] = 'X'
                raise
            if board[i][j] != 'E':
                return

            mine_count = 0
            for di, dj in directions:
                if valid_pos(i+di, j+dj) and board[i+di][j+dj] == 'M':
                    mine_count += 1

            if mine_count == 0:
                board[i][j] = 'B'
                for di, dj in directions:
                    if valid_pos(i+di, j+dj):
                        dfs(i+di, j+dj)
            else:
                board[i][j] = str(mine_count)

        try:
            dfs(click[0], click[1])
        except:
            pass

        return board


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        board = [['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'M', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E'],
                 ['E', 'E', 'E', 'E', 'E']]
        click = [3, 0]
        expected = [['B', '1', 'E', '1', 'B'],
                    ['B', '1', 'M', '1', 'B'],
                    ['B', '1', '1', '1', 'B'],
                    ['B', 'B', 'B', 'B', 'B']]
        self.assertCountEqual(sol.updateBoard(board, click), expected)

    def test_case_2(self):
        sol = Solution()
        board = [['B', '1', 'E', '1', 'B'],
                 ['B', '1', 'M', '1', 'B'],
                 ['B', '1', '1', '1', 'B'],
                 ['B', 'B', 'B', 'B', 'B']]
        click = [1, 2]
        expected = [['B', '1', 'E', '1', 'B'],
                    ['B', '1', 'X', '1', 'B'],
                    ['B', '1', '1', '1', 'B'],
                    ['B', 'B', 'B', 'B', 'B']]
        self.assertCountEqual(sol.updateBoard(board, click), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
