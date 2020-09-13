import unittest
from typing import List
from pprint import pprint


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val in {p.val, q.val}:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def sub(node):
            if not node:
                return False, None

            left, nl = sub(node.left)
            right, nr = sub(node.right)

            cur, n_cur = (True, node) if node.val in {
                p.val, q.val} else (False, None)

            if (left and right) or (left and cur) or (right and cur):
                return True, node
            else:
                return left or right or cur, nl or nr or n_cur

        found, ans = sub(root)
        return ans if found else None

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def sub(node):
            # return common_ancestor, found_p, found_q
            if not node:
                return None, False, False

            if node.val == p.val:
                _, _, left_found_q = sub(node.left)
                _, _, right_found_q = sub(node.right)
                if left_found_q or right_found_q:
                    return node, True, True
                else:
                    return None, True, False

            if node.val == q.val:
                _, left_found_p, _ = sub(node.left)
                _, right_found_p, _ = sub(node.right)
                if left_found_p or right_found_p:
                    return node, True, True
                else:
                    return None, False, True

            left_common_ancestor, left_found_p, left_found_q = sub(node.left)
            right_common_ancestor, right_found_p, right_found_q = sub(
                node.right)

            if left_common_ancestor or right_common_ancestor:
                return left_common_ancestor or right_common_ancestor, True, True
            else:
                if (left_found_p and right_found_q) or (left_found_q and right_found_p):
                    return node, True, True
                else:
                    return None, left_found_p or right_found_p, left_found_q or right_found_q

        common_ancestor, _, _ = sub(root)
        return common_ancestor


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
