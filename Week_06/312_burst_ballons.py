import unittest
from typing import List
from pprint import pprint


# def get_bit(value, n):
#     return ((value >> n & 1) != 0)

# def set_bit(value, n):
#     return value | (1 << n)

# def clear_bit(value, n):
#     return value & ~(1 << n)

# 查理芒格：反过来想，总是反过来想
# 核心难点：戳破气球以后，相邻的气球就变了
# 解决办法：
# 思考按顺序戳破气球的逆向过程，把一个个气球给加回来
# 解决的就是加回来的顺序问题了
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums = [1, ]+nums+[1, ]
        cache = {}

        def dp(left, right):
            if (left, right) in cache:
                return cache[(left, right)]
            if left + 1 == right:
                return 0

            res = max((nums[left]*nums[i]*nums[right] + dp(left, i) + dp(i, right))
                      for i in range(left+1, right))
            cache[(left, right)] = res
            return res

        return dp(0, len(nums)-1)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums = [3, 1, 5, 8]
        expected = 167
        self.assertEqual(sol.maxCoins(nums), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
