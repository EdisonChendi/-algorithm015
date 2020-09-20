import unittest
from typing import List
from pprint import pprint


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key=lambda p: (p[0], -p[1]), reverse=True)
        for p in people:
            h, k = p
            res.insert(k, p)
        return res


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
        expected = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        self.assertCountEqual(sol.reconstructQueue(people), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
