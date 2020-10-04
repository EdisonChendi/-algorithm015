import unittest
from typing import List
from pprint import pprint
from collections import Counter, OrderedDict, defaultdict, deque
from copy import copy


class Window:

    def __init__(self, S, T):
        self.S = S
        self.T = T
        self.copy_T = copy(T)
        self.window_dict = defaultdict(deque)
        self.covered = False
        self.l = -1
        self.r = -1

    def add(self, i):
        ch = self.S[i][1]
        if ch in self.T or ch in self.window_dict:

            if self.l == -1:
                self.l = i

            self.r = i
            self.S[i][2] = 1
            self.window_dict[ch].append(i)
            if len(self.window_dict[ch]) > self.copy_T[ch]:
                idx = self.window_dict[ch].popleft()
                self.S[idx][2] = 0
                while self.S[self.l][2] == 0:
                    self.l += 1

            if not self.covered and ch in self.T:
                self.T[ch] -= 1
                if self.T[ch] == 0:
                    del self.T[ch]
                if not self.T:
                    self.covered = True

            return True

        return False

    def len(self):
        return self.S[self.r][0] - self.S[self.l][0] + 1

    def boundary(self):
        return (self.S[self.l][0], self.S[self.r][0])

    def __repr__(self):
        return f"covered:{self.covered}, l: {self.l}, r:{self.r}, S: {self.S}"


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        S = [[i, ch, 0] for i, ch in enumerate(s) if ch in T]
        window = Window(S, T)
        min_l, min_l_boundary = 10e7, None
        # print(window)
        for i in range(len(S)):
            added = window.add(i)
            if added and window.covered:
                if window.len() < min_l:
                    min_l = window.len()
                    min_l_boundary = window.boundary()
            # print(window)
        if window.covered:
            return s[min_l_boundary[0]:min_l_boundary[1]+1]
        else:
            return ""


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        S = "ADOBCODEBANC"
        T = "ABC"
        expected = "BANC"
        self.assertEqual(sol.minWindow(S, T), expected)

    def test_case_2(self):
        sol = Solution()
        S = "bba"
        T = "ab"
        expected = "ba"
        self.assertEqual(sol.minWindow(S, T), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
