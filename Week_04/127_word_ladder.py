import unittest
from typing import List
from pprint import pprint
from collections import deque, defaultdict
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        len_w = len(beginWord)

        words = set(wordList)
        word_shapes = defaultdict(set)
        for w in words:
            for i in range(len_w):
                shape = w[:i] + "*" + w[i+1:]
                word_shapes[shape].add(w)

        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len_w):
                shape = word[:i] + "*" + word[i+1:]
                for w in word_shapes[shape]:
                    if w not in visited:
                        visited.add(w)
                        q.append((w, level+1))
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
