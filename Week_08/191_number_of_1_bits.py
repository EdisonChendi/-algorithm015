import unittest
from typing import List
from pprint import pprint


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n = n & (n-1)
        return count


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 0b00000000000000000000000000001011
        res = 3
        self.assertEqual(sol.hammingWeight(n), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
