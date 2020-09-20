import unittest
from typing import List
from pprint import pprint
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)

        def handle5(changes):
            changes[5] += 1
            return True

        def handle10(changes):
            if changes[5] > 0:
                changes[5] -= 1
                changes[10] += 1
                return True
            return False

        def handle20(changes):
            if changes[10] > 0 and changes[5] > 0:
                changes[10] -= 1
                changes[5] -= 1
                changes[20] += 1
                return True
            if changes[5] >= 3:
                changes[5] -= 3
                changes[20] += 1
                return True
            return False

        receive_and_change = {
            5: handle5,
            10: handle10,
            20: handle20
        }
        return all(receive_and_change[b](changes) for b in bills)


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        billis = [5, 5, 5, 10, 20]
        expected = True
        self.assertEqual(sol.lemonadeChange(billis), expected)

    def test_case_2(self):
        sol = Solution()
        billis = [5, 5, 10]
        expected = True
        self.assertEqual(sol.lemonadeChange(billis), expected)

    def test_case_3(self):
        sol = Solution()
        billis = [10, 10]
        expected = False
        self.assertEqual(sol.lemonadeChange(billis), expected)

    def test_case_4(self):
        sol = Solution()
        billis = [5, 5, 10, 10, 20]
        expected = False
        self.assertEqual(sol.lemonadeChange(billis), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
