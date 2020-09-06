import unittest
from typing import List
from pprint import pprint
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        primes = (2, 3, 5)
        ugly_nums = [1]
        seen.add(1)
        heapq.heapify(ugly_nums)
        i = 1
        while i <= n:
            ug = heapq.heappop(ugly_nums)
            for p in primes:
                prod = p*ug
                if prod not in seen:
                    seen.add(prod)
                    heapq.heappush(ugly_nums, prod)
            i += 1
        return ug


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 10
        expected = 12
        self.assertEqual(sol.nthUglyNumber(n), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
