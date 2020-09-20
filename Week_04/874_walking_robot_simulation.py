import unittest
from typing import List
from pprint import pprint

# trick
# turn right -> dx, dy = dy, -dx
# turn left -> dx, dy = -dy, dx

# Solution:
#
# class Solution(object):
#     def robotSim(self, commands, obstacles):
#         dx = [0, 1, 0, -1]
#         dy = [1, 0, -1, 0]
#         x = y = di = 0
#         obstacleSet = set(map(tuple, obstacles))
#         ans = 0

#         for cmd in commands:
#             if cmd == -2:  # left
#                 di = (di - 1) % 4
#             elif cmd == -1:  # right
#                 di = (di + 1) % 4
#             else:
#                 for k in xrange(cmd):
#                     if (x+dx[di], y+dy[di]) not in obstacleSet:
#                         x += dx[di]
#                         y += dy[di]
#                         ans = max(ans, x*x + y*y)

#         return ans


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def euc_dis(pos):
            return pos[0]**2 + pos[1]**2

        obstacles = set(tuple(o) for o in obstacles)
        pos = (0, 0)
        max_ = euc_dis(pos)
        dx, dy = 0, 1
        for cmd in commands:
            if cmd == -1:
                dx, dy = dy, -dx
            elif cmd == -2:
                dx, dy = -dy, dx
            else:
                for _ in range(cmd):
                    nxt_pos = (pos[0]+dx, pos[1]+dy)
                    if nxt_pos in obstacles:
                        break
                    pos = nxt_pos
            max_ = max(max_, euc_dis(pos))
        return max_


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        commands = [4, -1, 3]
        obstacles = []
        expected = 25
        self.assertEqual(sol.robotSim(commands, obstacles), expected)

    def test_case_2(self):
        sol = Solution()
        commands = [4, -1, 4, -2, 4]
        obstacles = [[2, 4]]
        expected = 65
        self.assertEqual(sol.robotSim(commands, obstacles), expected)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
