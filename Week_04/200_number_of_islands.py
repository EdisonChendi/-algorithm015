import unittest
from typing import List
from pprint import pprint


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if grid[i][j] == '0':
                return

            grid[i][j] = '0'
            for di, dj in directions:
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < height and 0 <= new_j < width:
                    dfs(new_i, new_j)

        if not grid:
            return 0
        count = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        width, height = len(grid[0]), len(grid)
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == '1':
                    dfs(i, j)
                    count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        expected = 1
        self.assertEqual(sol.numIslands(grid), expected)

    def test_case_2(self):
        sol = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        expected = 3
        self.assertEqual(sol.numIslands(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
