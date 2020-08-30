import unittest
from typing import List
from pprint import pprint


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        plus_one = 1
        for n in reversed(digits):
            nn = n + carry + plus_one
            plus_one = 0
            carry, nn = (1, nn % 10) if nn >= 10 else (0, nn)
            # can do early return
            res.append(nn)
        if carry > 0:
            res.append(1)
        return list(reversed(res))


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        digits = [1, 2, 3]
        ans = [1, 2, 4]
        self.assertListEqual(sol.plusOne(digits), ans)

    def test_case_2(self):
        sol = Solution()
        digits = [9, 9, 9]
        ans = [1, 0, 0, 0]
        self.assertListEqual(sol.plusOne(digits), ans)

    def test_case_3(self):
        sol = Solution()
        digits = [8, 9, 9, 9]
        ans = [9, 0, 0, 0]
        self.assertListEqual(sol.plusOne(digits), ans)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
