class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k
        self.size = 0
        self.arr = [0]*k
        self.f = 0
        self.e = k-1

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.f > 0:
            self.f -= 1
        else:
            self.f = self.cap - 1
        self.arr[self.f] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.e < self.cap - 1:
            self.e += 1
        else:
            self.e = 0
        self.arr[self.e] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.f == self.cap-1:
            self.f = 0
        else:
            self.f += 1
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.e == 0:
            self.e = self.cap-1
        else:
            self.e -= 1
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.f]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[self.e]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
circularDeque = MyCircularDeque(3)
assert circularDeque.insertLast(1) == True
assert circularDeque.insertLast(2) == True
assert circularDeque.insertFront(3) == True
assert circularDeque.insertFront(4) == False
assert circularDeque.getRear() == 2
assert circularDeque.isFull() == True
assert circularDeque.deleteLast() == True
assert circularDeque.insertFront(4) == True
assert circularDeque.getFront() == 4
