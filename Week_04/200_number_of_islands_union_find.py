import unittest
from typing import List
from pprint import pprint


class UnionFind:

    def __init__(self, n):
        self.arr = [None]*n
        for i in range(n):
            self.arr[i] = i

    def union(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        self.arr[root_j] = root_i

    def is_connected(self, i, j):
        root_i = self.find_root(i)
        root_j = self.find_root(j)
        return root_i == root_j

    def find_root(self, i):
        root = i
        while self.arr[root] != root:
            root = self.arr[root]
        # do compression
        while self.arr[i] != i:
            i, self.arr[i] = self.arr[i], root
        return root


# class TestUnionFind(unittest.TestCase):

    # def test_case_1(self):
    #     uf = UnionFind(8)
    #     uf.union(0, 1)
    #     uf.union(0, 2)
    #     uf.union(0, 3)
    #     uf.union(0, 7)
    #     self.assertTrue(uf.is_connected(1, 7))
    #     uf.union(4, 5)
    #     uf.union(4, 6)
    #     self.assertTrue(uf.is_connected(4, 6))
    #     self.assertFalse(uf.is_connected(1, 6))
    #     uf.union(6, 3)
    #     self.assertTrue(uf.is_connected(1, 5))

    # def test_case_1(self):
    #     uf = UnionFind(4)
    #     uf.union(2, 3)
    #     uf.union(0, 1)
    #     uf.union(1, 2)
    #     print(uf.arr)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        height, width = len(grid), len(grid[0])

        def d(i, j):
            return i*width+j

        def valid_pos(i, j):
            return 0 <= i < height and 0 <= j < width

        uf = UnionFind(d(height, width))

        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == '1':
                    for di, dj in ((0, -1), (-1, 0)):
                        new_i, new_j = (i+di, j+dj)
                        if valid_pos(new_i, new_j) and grid[new_i][new_j] == '1':
                            uf.union(d(i, j), d(new_i, new_j))

        roots = set()
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == '1':
                    roots.add(uf.find_root(d(i, j)))

        return len(roots)


class TestSolution(unittest.TestCase):
    # class estSolution:

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

    # def test_case_2(self):
    #     sol = Solution()
    #     grid = [
    #         ["1", "1", "0", "0", "0"],
    #         ["1", "1", "0", "0", "0"],
    #         ["0", "0", "1", "0", "0"],
    #         ["0", "0", "0", "1", "1"]
    #     ]
    #     expected = 3
    #     self.assertEqual(sol.numIslands(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
