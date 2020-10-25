import unittest
from typing import List
from pprint import pprint
from heapq import heapify, heappop


class Leaderboard:

    def __init__(self):
        self.board = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.board[playerId] += score
        else:
            self.board[playerId] = score

    def top(self, K: int) -> int:
        heap = list(-v for v in self.board.values())
        heapify(heap)
        return -sum(heappop(heap) for _ in range(min(K, len(heap))))

    def reset(self, playerId: int) -> None:
        self.board.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        pass

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
