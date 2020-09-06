import unittest
from typing import List
from pprint import pprint

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        prev_level = [root, ]
        while prev_level:
            prev_level_res = []
            cur_level = []
            for node in prev_level:
                prev_level_res.append(node.val)
                cur_level.extend(node.children)
            res.append(prev_level_res)
            prev_level = cur_level
        return res

    def levelOrder1(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            node, level = q.popleft()
            if (len(res)-1) < level:
                res.append([])
            res[level].append(node.val)
            for c in node.children:
                q.append((c, level+1))
        return res

    def levelOrder2(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            cur_level = []
            cur_level_length = len(q)
            for _ in range(cur_level_length):
                node = q.pop()
                cur_level.append(node.val)
                q.extend(node.children)
            res.append(cur_level)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
