import unittest
from typing import List
from pprint import pprint


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {0}
        ans = 0
        seen = set()
        while dp:
            ans += 1
            new_dp = set()
            for n in dp:
                for c in coins:
                    if n + c == amount:
                        return ans
                    if n + c < amount and n + c not in seen:
                        seen.add(n+c)
                        new_dp.add(n+c)
            dp = new_dp
        return -1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        self.assertEqual(sol.coinChange(coins, amount), expected)

    def test_case_2(self):
        sol = Solution()
        coins = [2]
        amount = 3
        expected = -1
        self.assertEqual(sol.coinChange(coins, amount), expected)

    def test_case_3(self):
        sol = Solution()
        coins = [1]
        amount = 0
        expected = 0
        self.assertEqual(sol.coinChange(coins, amount), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
