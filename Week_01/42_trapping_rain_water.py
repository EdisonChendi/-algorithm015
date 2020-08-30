import unittest
from typing import List
from pprint import pprint


class Solution:
    def trap1(self, height: List[int]) -> int:
        # every bar position can trap how much water?
        # min(left bound, right bound) - bar_height
        # left bound is max(left-side)
        # right bound is max(right-side)
        # scan whole list twice -> left_bounds AND right_bounds

        def bounds(height):
            res = []
            max_ = -1
            for h in height:
                max_ = max([h, max_])
                res.append(max_)
            return res

        return sum(min(l, r) - h
                   for l, r, h in zip(bounds(height),
                                      reversed(bounds(reversed(height))),
                                      height))

    def trap(self, height: List[int]) -> int:
        # ok... Two pointers is even better
        if not height or len(height) <= 2:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        ans = 0
        while left < right:
            if left_max < right_max:
                ans += left_max-height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                ans += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return ans


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected = 6
        self.assertEqual(sol.trap(height), expected)

    def test_edge_case_1(self):
        sol = Solution()
        height = []
        expected = 0
        self.assertEqual(sol.trap(height), expected)

    def test_edge_case_2(self):
        sol = Solution()
        height = [1]
        expected = 0
        self.assertEqual(sol.trap(height), expected)

    def test_edge_case_3(self):
        sol = Solution()
        height = [1, 3]
        expected = 0
        self.assertEqual(sol.trap(height), expected)


if __name__ == "__main__":
    unittest.main()
