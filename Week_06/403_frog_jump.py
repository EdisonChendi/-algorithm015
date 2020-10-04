import unittest
from typing import List
from pprint import pprint
from heapq import heappop, heappush
from collections import defaultdict


class Solution:
    def canCross2(self, stones: List[int]) -> bool:
        q = []
        target = stones[-1]
        seen = set()
        stones = set(stones)

        q.append((0, 0))
        seen.add((0, 0))

        while q:
            # print(q)
            pos, jump = heappop(q)
            if pos == target:
                return True
            jump = -jump
            jumps = filter(lambda x: x[0] > 0 and x[1] < 0,
                           ((pos+jump+j, -jump-j) for j in [-1, 0, 1]))
            # print(list(jumps))
            for j in jumps:
                if j[0] in stones and j not in seen:
                    seen.add(j)
                    heappush(q, j)
        return False

    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        sizes = defaultdict(set)
        sizes[0].add(0)
        for i, s in enumerate(stones):
            for jump in sizes[s]:
                for choice in (jump-1, jump, jump+1):
                    if choice > 0 and (s+choice) in stones_set:
                        sizes[s+choice].add(choice)
        return bool(sizes[stones[-1]])


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        stones = [0, 1, 3, 5, 6, 8, 12, 17]
        expected = True
        self.assertEqual(sol.canCross(stones), expected)

    def test_case_2(self):
        sol = Solution()
        stones = [0, 1, 2, 3, 4, 8, 9, 11]
        expected = False
        self.assertEqual(sol.canCross(stones), expected)

    def test_case_3(self):
        sol = Solution()
        stones = [0, 2]
        expected = False
        self.assertEqual(sol.canCross(stones), expected)

    def test_case_4(self):
        sol = Solution()
        stones = [0, 1, 3, 6, 10, 13, 15, 18]
        expected = True
        self.assertEqual(sol.canCross(stones), expected)

    def test_edge_case_1(self):
        sol = Solution()
        stones = [0]
        expected = True
        self.assertEqual(sol.canCross(stones), expected)


if __name__ == "__main__":
    unittest.main()
