class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        # self.data = [0 for i in range(k)]
        self.data = [0] * k
        self.head = -1
        self.tail = -1
        # self.cnt = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head += 1
        self.tail = (self.tail + 1) % len(self.data)

        self.data[self.tail] = value
        # self.cnt += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        de = self.data[self.head]
        print('head:',self.head)
        print('del:',de)
        self.head = (self.head + 1) % len(self.data)

        if self.head == (self.tail + 1) % len(self.data):
            self.head = -1
            self.tail = -1
            print('reset!!!!!!!!!!!')
        # self.cnt -= 1
        return True

        # 因为出队并不需要返回值，也可以按下边这种逻辑，出队之前两者相同，出队操作就可以直接重置，也就省了模运算而已。
        # if (head == tail) {
        # head = -1;
        # tail = -1;
        # return true;
        # }


    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        # return self.head == self.tail and self.head == -1
        return self.head == -1#既然做过特殊处理，就不需要区分是空还是有一个了，head==-1就等于空
        # return self.cnt == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        # print('is full?tail:{0},head{1}'.format(self.tail,self.head))

        return ((self.tail + 1) % len(self.data)) == self.head
        # return self.cnt == len(self.data)

# 速度快的答案是用list直接append和del，但是太犯规了，就是设计循环队列
# 靠计数器判断也太赖了，也删了，只要注意清空重置操作（是否重置为-1也不是特别重要，相同最重要）
# 还有就是重置的和判定条件，不是head比tail大，是head+1的模运算等于tail

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())
print(obj.deQueue())
print(obj.deQueue())
print(obj.deQueue())



