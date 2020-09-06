import unittest
from typing import List
from pprint import pprint


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def sub(node):
            if not node:
                return

            res.append(node.val)
            for c in node.children:
                sub(c)

        sub(root)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
