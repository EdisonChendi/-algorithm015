import unittest
from typing import List
from pprint import pprint
from collections import defaultdict 

class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def in_board(i, j):
            return 0 <= i < H and 0 <= j < W

        def dfs(res, i, j, cur_str, cur_node):
            ch = board[i][j]
            if ch not in cur_node.children:
                return

            board[i][j] = "#"
            next_node = cur_node.children[ch]
            next_str = cur_str + ch
            if next_node.is_word:
                res.add(next_str)
            for di, dj in directions:
                x, y = i+di, j+dj
                if in_board(x, y) and board[x][y] != "#":
                    dfs(res, x, y, next_str, next_node)
            board[i][j] = ch

        if not board or not words:
            return []

        # STEP1: build trie
        trie = Trie()
        for w in words:
            trie.insert(w)

        # STEP2: walk the board, run dfs on each element
        res = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        H, W = len(board), len(board[0])
        for i in range(H):
            for j in range(W):
                dfs(res, i, j, "", trie.root)
        return list(res)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        words = ["oath", "pea", "eat", "rain"]
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ]
        expected = ["eat", "oath"]
        self.assertEqual(sol.findWords(board, words), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
