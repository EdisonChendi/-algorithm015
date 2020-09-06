import unittest
from typing import List
from pprint import pprint
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            counter = [0, ]*26
            for ch in s:
                counter[ord(ch)-ord('a')] += 1
            groups[tuple(counter)].append(s)
        return list(groups.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[tuple(sorted(Counter(s).items()))].append(s)
        return list(groups.values())


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        ans = sol.groupAnagrams(strs)
        print(ans)

    def test_case_2(self):
        sol = Solution()
        strs = [""]
        expected = [[""]]
        ans = sol.groupAnagrams(strs)
        print(ans)

    def test_case_3(self):
        sol = Solution()
        strs = ["a"]
        expected = [["a"]]
        ans = sol.groupAnagrams(strs)
        print(ans)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
