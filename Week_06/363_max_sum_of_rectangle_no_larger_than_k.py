import unittest
from typing import List
from pprint import pprint
import math
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        def sub(row):
            # find subarray sum closest to k
            N = len(row)
            pre_sum = [0]*(N+1)
            for i in range(1, N+1):
                pre_sum[i] = pre_sum[i-1]+row[i-1]
            # print(f"pre_sum:{pre_sum}")
            seen = [pre_sum[0], ]
            res = -math.inf
            for i in range(1, N+1):
                s = pre_sum[i]
                complement = s-k
                idx = bisect.bisect_right(seen, complement)
                # print(f"i:{i}, idx:{idx}, seen:{seen}")
                if idx > 0 and seen[idx-1] == complement:
                    return k
                elif idx < len(seen):
                    cur_res = s-seen[idx]
                    if cur_res > res:
                        res = cur_res
                bisect.insort_right(seen, s)
            return res

        W, H = len(matrix[0]), len(matrix)
        res = -math.inf
        for i in range(W):
            col = [0]*H
            for j in range(i, W):
                # print("--------"*5)
                col = [(col[l]+matrix[l][j]) for l in range(H)]
                # print(col)
                cur_res = sub(col)
                if cur_res > res:
                    res = cur_res
                # print(f"i:{i}, j:{j}, cur_res: {cur_res}, res:{res}")
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        matrix = [[1, 0, 1], [0, -2, 3]]
        k = 2
        expected = 2
        self.assertEqual(sol.maxSumSubmatrix(matrix, k), expected)

    def test_case_2(self):
        sol = Solution()
        matrix = [[1, ], ]
        k = 1
        expected = 1
        self.assertEqual(sol.maxSumSubmatrix(matrix, k), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
