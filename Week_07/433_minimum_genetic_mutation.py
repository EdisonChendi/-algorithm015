import unittest
from typing import List
from pprint import pprint


class Solution:
    def minMutation2(self, start: str, end: str, bank: List[str]) -> int:
        # one-way bfs
        N = 8
        G = ('A', 'C', 'G', 'T')
        bank = set(bank)
        count = 0
        q = [start]
        while q:
            next_q = []
            while q:
                gene = q.pop()
                if gene == end:
                    return count
                for i in range(8):
                    for g in G:
                        n_gene = gene[:i] + g + gene[i+1:]
                        if n_gene in bank:
                            bank.remove(n_gene)
                            next_q.append(n_gene)
            count += 1
            q = next_q
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # two-way bfs
        N = 8
        G = ('A', 'C', 'G', 'T')
        bank = set(bank)
        count = 0

        if end not in bank:
            return -1

        front = {"s": {start, }, "v": {start, }}
        back = {"s": {end, }, "v": {end, }}

        while front["s"]:
            visited = front["v"]
            next_front = set()
            for gene in front["s"]:
                if gene in back["s"]:
                    return count
                for i in range(8):
                    for g in G:
                        n_gene = gene[:i] + g + gene[i+1:]
                        if n_gene in bank and n_gene not in visited:
                            visited.add(n_gene)
                            next_front.add(n_gene)
            count += 1
            front["s"] = next_front
            if len(front["s"]) > len(back["s"]):
                front, back = back, front
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        start = "AACCGGTT"
        end = "AACCGGTA"
        bank = ["AACCGGTA"]
        expected = 1
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_2(self):
        sol = Solution()
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        expected = 2
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_3(self):
        sol = Solution()
        start = "AAAAAAAA"
        end = "CCCCCCCC"
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC",
                "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]
        expected = -1
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_4(self):
        sol = Solution()
        start = "AAAAAAAA"
        end = "CCCCCCCC"
        bank = ["AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC",
                "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA", "CCCCCCCC"]
        expected = 8
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    def test_case_5(self):
        sol = Solution()
        start = "AAAACCCC"
        end = "CCCCCCCC"
        bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC",
                "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]
        expected = 4
        self.assertEqual(sol.minMutation(start, end, bank), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
