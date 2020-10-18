import unittest
from typing import List
from pprint import pprint
from collections import deque


class UnionFind:

    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    def find(self, p):
        root = p
        while self.parent[root] != root:
            root = self.parent[root]
        # compression
        while p != root:
            p, self.parent[p] = self.parent[p], root
        return root

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
        self.count -= 1


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        # by union find
        if not grid or not grid[0]:
            return 0
        H, W = len(grid), len(grid[0])
        uf = UnionFind(H*W)
        water = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '1':
                    grid[i][j] = '2'
                    cur = i*W+j
                    if i > 0 and grid[i-1][j] == '2':
                        uf.union(cur, cur-W)
                    if j > 0 and grid[i][j-1] == '2':
                        uf.union(cur, cur-1)
                else:
                    water += 1
        return uf.count - water

    def numIslands2(self, grid: List[List[str]]) -> int:
        # by bfs
        if not grid or not grid[0]:
            return 0
        H, W = len(grid), len(grid[0])
        res = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '0':
                    continue
                res += 1
                q = deque()
                q.append((i, j))
                grid[i][j] = '0'
                while q:
                    ii, jj = q.popleft()
                    for di, dj in directions:
                        ni, nj = ii+di, jj+dj
                        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '1':
                            grid[ni][nj] = '0'
                            q.append((ni, nj))
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        # by dfs
        def dfs(i, j):
            if 0 <= i < H and 0 <= j < W and grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)

        if not grid or not grid[0]:
            return 0
        H, W = len(grid), len(grid[0])
        res = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '0':
                    continue
                res += 1
                dfs(i, j)
        return res


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

    def test_case_3(self):
        sol = Solution()
        grid = [
            ["1", "1", "1"],
            ["1", "0", "1"],
            ["1", "1", "1"]
        ]
        expected = 1
        self.assertEqual(sol.numIslands(grid), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
