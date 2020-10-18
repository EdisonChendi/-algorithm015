import unittest
from typing import List
from pprint import pprint


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
    def findCircleNum1(self, M: List[List[int]]) -> int:
        # by union find
        N = len(M)
        uf = UnionFind(N)
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.count

    def findCircleNum(self, M: List[List[int]]) -> int:
        # by dfs
        def dfs(i):
            for j in range(N):
                if M[i][j] == 1:
                    M[i][j] = 0
                    dfs(j)

        count = 0
        N = len(M)
        for i in range(N):
            if M[i][i] == 1:
                dfs(i)
                count += 1
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        M = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
        expected = 2
        self.assertEqual(sol.findCircleNum(M), expected)

    def test_case_2(self):
        sol = Solution()
        M = [[1, 1, 1],
             [1, 1, 1],
             [1, 1, 1]]
        expected = 1
        self.assertEqual(sol.findCircleNum(M), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
