import unittest
from typing import List
from pprint import pprint
import heapq
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = []
        for n, c in collections.Counter(nums).items():
            heapq.heappush(counter, (-c, n))
        res = []
        for _ in range(k):
            _, n = heapq.heappop(counter)
            res.append(n)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertListEqual(sol.topKFrequent(nums, k), expected)

    def test_case_2(self):
        sol = Solution()
        nums = [1]
        k = 1
        expected = [1]
        self.assertListEqual(sol.topKFrequent(nums, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
