# 用栈实现队列
class MyQueue_myself:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack_in.append(x)
        if self.stack_out == []:#如果空了就把in都移过来
            while self.stack_in != []:
                self.stack_out.append(self.stack_in.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        ret = None
        if self.stack_out != []:
            ret =  self.stack_out.pop()
        if self.stack_out == []:#如果空了就把in都移过来
            while self.stack_in != []:
                self.stack_out.append(self.stack_in.pop())
        if ret == None and self.stack_out != []:
            ret =  self.stack_out.pop()
        return ret

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.stack_out != []:
            return self.stack_out[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.stack_out != []:
            return False
        return True
class MyQueue:
    def __init__(self):
        self.data = []
    def push(self, x):
        temp = []
        while self.data:
            temp.append(self.data.pop())
        temp.append(x)
        while temp:
            self.data.append(temp.pop())
        return
    def pop(self):
        if self.data:
            return self.data.pop()
        return 0
    def peek(self):
        if self.data:
            return self.data[-1]
        return 0
    def empty(self):
        return not self.data



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
# print(obj.pop())
print(obj.empty())