import unittest
from typing import List
from pprint import pprint
import math


class Solution:
    def splitArray2(self, nums: List[int], m: int) -> int:
        # top down DP - seems pretty slow

        def cal_pre_sums(nums):
            N = len(nums)
            pre_sum = [0]*N
            for i in range(N):
                pre_sum[i] = nums[i] + (pre_sum[i-1] if i > 0 else 0)
            return pre_sum

        def pre_sum(i, j):
            # arr[i] + arr[i+1] + ... arr[j]
            assert i <= j
            return pre_sums[j] - (pre_sums[i-1] if i > 0 else 0)

        def sub(start, end, m):
            if (start, end, m) in cache:
                return cache[(start, end, m)]

            if m == 1:
                return pre_sums[end] - (pre_sums[start-1] if start > 0 else 0)

            res = math.inf
            for i in range(start, end-m+2):
                first = pre_sums[i]-(pre_sums[start-1] if start > 0 else 0)
                rest_total = pre_sums[end] - pre_sums[i]
                if first >= rest_total:
                    res = min(first, res)
                    break
                j = i+1
                while nums[j] == 0:
                    j += 1
                rest = sub(j, end, m-1)
                res = min(res, max(first, rest))

            cache[(start, end, m)] = res
            return res

        cache = {}
        pre_sums = cal_pre_sums(nums)

        return sub(0, len(nums)-1, m)

    def splitArray2(self, nums: List[int], m: int) -> int:
        # bottom-up DP
        # dp[i][j] - split nums[:i] into j parts
        # dp[i][j] = max(dp[k][j-1], sum nums k+1 -> i)
        # .           for k up to i-1, choos minimum
        N = len(nums)

        # sum of first N numbers of nums
        pre_sums = [0]*(N+1)
        for i in range(1, N+1):
            pre_sums[i] = pre_sums[i-1] + nums[i-1]

        # dp table
        dp = [[math.inf] * (m+1) for _ in range(N+1)]

        # iteration
        dp[0][0] = 0
        for i in range(1, N+1):
            for j in range(1, m+1):
                dp[i][j] = min(
                    max(dp[k][j-1], pre_sums[i]-pre_sums[k])
                    for k in range(i)
                )
                # pprint(dp)

        return dp[-1][-1]

    def splitArray(self, nums: List[int], m: int) -> int:
        # binary search + greedy
        def can_split(mid):
            count, cur_sum = 0, 0
            for n in nums:
                if n > mid:
                    return False
                if cur_sum + n > mid:
                    count += 1
                    cur_sum = n
                else:
                    cur_sum += n
            count += 1
            return count <= m

        l, r = 0, sum(nums)
        ans = math.inf
        while l <= r:
            mid = (l+r)//2
            if can_split(mid):
                r = mid - 1
                ans = min(ans, mid)
            else:
                l = mid + 1
        return ans


class TestSolution(unittest.TestCase):

    # def test_case_1(self):
    #     sol = Solution()
    #     nums = [7, 2, 5, 10, 8]
    #     m = 2
    #     expected = 18
    #     self.assertEqual(sol.splitArray(nums, m), expected)

    # def test_case_2(self):
    #     sol = Solution()
    #     nums = [1, 2, 3, 4, 5]
    #     m = 2
    #     expected = 9
    #     self.assertEqual(sol.splitArray(nums, m), expected)

    # def test_case_3(self):
    #     sol = Solution()
    #     nums = [1, 4, 4]
    #     m = 3
    #     expected = 4
    #     self.assertEqual(sol.splitArray(nums, m), expected)

    def test_case_4(self):
        sol = Solution()
        nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 250, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 350, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 450, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 550, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 700, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 750, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 850, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 900, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 950, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        m = 50
        expected = 950
        self.assertEqual(sol.splitArray(nums, m), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
