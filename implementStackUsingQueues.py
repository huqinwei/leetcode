
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.length = 0
        self.top_ = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.length += 1
        self.top_ = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        if self.length == 0:
            return None
        tmp = deque()
        new_top = 0
        for _ in range(self.length - 1):
            new_top = self.queue.popleft()
            tmp.append(new_top)

        self.top_ = new_top

        ret = self.queue.popleft()
        self.queue = tmp
        self.length -= 1


        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.length == 0
# dq = deque()
# for i in range(5):
#     dq.append(i)
# print(dq)
# print(len(dq))
# dq_tmp = deque()
# for j in range(len(dq)-1):
#     dq_tmp.append(dq.popleft())
# print(dq.popleft())#last
# dq = dq_tmp
# print(dq)

obj = MyStack()
obj.push(4)
obj.push(6)
print(obj.pop())
obj.push(5)
print(obj.pop())
top = obj.top()
print(top)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()