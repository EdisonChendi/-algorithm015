import unittest
from typing import List
from pprint import pprint
from collections import deque, Counter
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        N = n
        heap = [(-n, t, None) for t, n in Counter(tasks).items()]
        heapify(heap)
        # waiting = deque([None]*(N+1))
        waiting = deque()
        time = 0
        history = []

        # print(heap, waiting, time)
        while heap or waiting:
            # print('=============================')
            if heap:
                # one tick
                n, t, _ = heappop(heap)
                history.append(t)
                n += 1
                time += 1
                if n != 0:
                    waiting.append((n, t, time))  # last execution timestamp
                while waiting and time-waiting[0][2] >= N:
                    task = waiting.popleft()
                    heappush(heap, task)
            else:
                assert bool(waiting)
                if time-waiting[0][2] < N:
                    idle = N-(time-waiting[0][2])
                    time += idle
                history.extend(["idle"]*(idle))
                # print(f"{idle} unit idle")
                heappush(heap, waiting.popleft())
            # print(heap, waiting, time)
            # print(f"history: {history}")

        return time

    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = sorted(Counter(tasks).values())
        max_ = cnts.pop()-1
        idle = max_*n
        i = 0
        while idle > 0 and i < len(cnts):
            idle -= min(max_, cnts[i])
            i += 1
        idle = max(idle, 0)
        return len(tasks) + idle


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        sol = Solution()
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 0
        expected = 6
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_case_2(self):
        sol = Solution()
        tasks = ["A", "A", "A", "B", "B", "B"]
        n = 2
        expected = 8
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_case_3(self):
        sol = Solution()
        tasks = tasks = ["A", "A", "A", "A", "A",
                         "A", "B", "C", "D", "E", "F", "G"]
        n = 2
        expected = 16
        self.assertEqual(sol.leastInterval(tasks, n), expected)

    def test_case_4(self):
        sol = Solution()
        tasks = ["A", "A", "A", "A", "A", "A"]
        n = 1
        expected = 11
        self.assertEqual(sol.leastInterval(tasks, n), expected)
    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
