from collections import OrderedDict
import unittest
from typing import List
from pprint import pprint


class ListNode:
    def __init__(self, k, v, prev=None, nxt=None):
        self.k = k
        self.v = v
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        v = self._cache[key]
        del self._cache[key]
        self._cache[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            del self._cache[key]
        else:
            if len(self._cache) == self._cap:
                lru = next(iter(self._cache.keys()))
                del self._cache[lru]
        self._cache[key] = value


class LRUCache1:

    def __init__(self, capacity: int):
        self._cap = capacity
        self._size = 0
        self.map = {}
        self.ll = ListNode(None, None)
        self.tail = None

    def _evit(self):
        if self._size == 0:
            return

        self._size -= 1
        self.map.pop(self.tail.k)
        prev = self.tail.prev
        if prev is self.ll:
            self.tail = None
        prev.nxt = None
        self.tail = prev

    def _get(self, key: int) -> ListNode:
        node = self.map[key]
        if node is not self.ll.nxt:
            prev, nxt = node.prev, node.nxt
            prev.nxt = nxt
            if nxt:
                nxt.prev = prev
            old_head = self.ll.nxt
            node.prev, node.nxt = self.ll, old_head
            self.ll.nxt, old_head.prev = node, node
            if node is self.tail:
                self.tail = prev
        else:
            pass

        return node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        return self._get(key).v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self._get(key)
            node.v = value
            return

        if self._size == self._cap:
            self._evit()

        h = ListNode(key, value, self.ll, self.ll.nxt)
        self.map[key] = h
        if self._size > 0:
            self.ll.nxt.prev = h
            self.ll.nxt = h
            self._size += 1
        else:
            self._size = 1
            self.ll.nxt = h
            self.tail = h


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertEqual(lRUCache.get(1), 1)
        # LRU key was 2, evicts key 2, cache is {1 = 1, 3 = 3}
        lRUCache.put(3, 3)
        self.assertEqual(lRUCache.get(2), -1)
        # LRU key was 1, evicts key 1, cache is {4 = 4, 3 = 3}
        lRUCache.put(4, 4)
        self.assertEqual(lRUCache.get(1), -1)  # return -1 (not found)
        self.assertEqual(lRUCache.get(3), 3)
        self.assertEqual(lRUCache.get(4), 4)

    # def test_edge_case_1(self):
    #     s = Solution()


if __name__ == "__main__":
    unittest.main()
