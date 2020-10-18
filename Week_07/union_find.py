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
        self.parent[p_root] = q_root
        self.count -= 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        # sol = Solution()
        uf = UnionFind(8)
        uf.union(1, 2)
        self.assertEqual(uf.find(1), uf.find(2))
        self.assertEqual(uf.count, 7)
        uf.union(3, 2)
        self.assertEqual(uf.find(1), uf.find(2))
        self.assertEqual(uf.find(1), uf.find(3))
        self.assertEqual(uf.count, 6)
        self.assertFalse(uf.find(0), uf.find(3))

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
