import unittest
from typing import List
from pprint import pprint


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            res = res ^ (n & 1)  # get most right bit
            n = n >> 1
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        n = 0b00000010100101000001111010011100
        res = 0b00111001011110000010100101000000
        self.assertEqual(sol.reverseBits(n), res)

    def test_case_2(self):
        sol = Solution()
        n = 0b11111111111111111111111111111101
        res = 0b10111111111111111111111111111111
        self.assertEqual(sol.reverseBits(n), res)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
