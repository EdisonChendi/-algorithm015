import unittest
from typing import List
from pprint import pprint


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        W, H = len(matrix[0]), len(matrix)
        dp = [0]*(W+1)
        max_length = 0
        for i in range(H):
            new_dp = [0]*(W+1)
            for j in range(1, W+1):
                if matrix[i][j-1] == '1':
                    new_dp[j] = 1 + min(new_dp[j-1], dp[j], dp[j-1])
                    max_length = max(max_length, new_dp[j])
            dp = new_dp
        return max_length**2


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0],
        ]
        expected = 4
        self.assertEqual(sol.maximalSquare(matrix), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
