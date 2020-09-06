import unittest
from typing import List
from pprint import pprint
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            return Counter(s) == Counter(t)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        s = "anagram"
        t = "nagaram"
        expected = True
        self.assertEqual(sol.isAnagram(s, t), expected)

    def test_case_2(self):
        sol = Solution()
        s = "rat"
        t = "car"
        expected = False
        self.assertEqual(sol.isAnagram(s, t), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
