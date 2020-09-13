import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse()
        inorder_map = {n: i for i, n in enumerate(inorder)}

        def sub(start, end):
            if start > end:
                return

            idx = inorder_map[preorder[-1]]
            return TreeNode(preorder.pop(), sub(start, idx-1), sub(idx+1, end))

        return sub(0, len(inorder)-1)

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder.reverse()

        def sub(inorder):
            if not inorder:
                return

            # this is slow, use a map to speed up
            idx = inorder.index(preorder[-1])
            return TreeNode(preorder.pop(), sub(inorder[:idx]), sub(inorder[idx+1:]))

        return sub(inorder)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
