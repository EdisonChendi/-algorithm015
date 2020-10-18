import unittest
from typing import List
from pprint import pprint
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        patterns = defaultdict(set)
        contains_end_word = False
        for w in wordList:
            if w == endWord:
                contains_end_word = True
            for i in range(len(w)):
                pat = w[:i] + '*' + w[i+1:]
                patterns[pat].add(w)

        if not contains_end_word:
            return 0
        if beginWord == endWord:
            return 1

        front, back, visited = {beginWord, }, {endWord, }, {beginWord, endWord}
        count = 1
        while front:
            next_front = set()
            for w in front:
                for i in range(len(w)):
                    pat = w[:i] + '*' + w[i+1:]
                    for nw in patterns[pat]:
                        if nw in back:
                            return count + 1
                        if nw not in visited:
                            visited.add(nw)
                            next_front.add(nw)
                    patterns.pop(pat)
            count += 1
            front = next_front
            if len(front) > len(back):
                front, back = back, front

        return 0


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        expected = 5
        self.assertEqual(sol.ladderLength(
            beginWord, endWord, wordList), expected)

    def test_case_2(self):
        sol = Solution()
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        expected = 0
        self.assertEqual(sol.ladderLength(
            beginWord, endWord, wordList), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
