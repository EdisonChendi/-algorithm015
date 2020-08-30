import unittest
from typing import List
from pprint import pprint

# can't use Python slice - shallow array copy - extra space


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # move from end to begin
        i, i1, i2 = len(nums1)-1, m-1, n-1
        while i1 >= 0 and i2 >= 0:
            if nums2[i2] >= nums1[i1]:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
            i -= 1
        while i2 >= 0:
            nums1[i] = nums2[i2]
            i2 -= 1
            i -= 1

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 1. move nums1 ele -> end
        for i in range(m):
            nums1[len(nums1)-1-i] = nums1[m-1-i]
        # 2. merge
        i, i1, i2 = 0, len(nums1)-m, 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
            i += 1
        # 3. handle remains
        while i2 < len(nums2):
            nums1[i] = nums2[i2]
            i += 1
            i2 += 1


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        expected = [1, 2, 2, 3, 5, 6]

    def test_case_2(self):
        sol = Solution()
        nums1 = [1, 2, 4, 5, 6, 0]
        m = 5
        nums2 = [3]
        n = 1
        expected = [1, 2, 3, 4, 5, 6]

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
