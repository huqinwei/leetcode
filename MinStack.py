# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
#         self.min_val = 0
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         if self.data == []:
#             self.min_val = x
#         self.data.append(x)
#         self.min_val = min(self.min_val,x)
#
#     # 考虑到要求用常数时间找到最小值，就不可能去用什么i in list的逻辑去查找了，所以维护了一个最小值，在入栈和出栈时维护，不过仍然不是最优。
#     def pop(self):
#         """
#         :rtype: void
#         """
#         if self.data != []:
#             ret =  self.data.pop()
#             if self.data != []:
#                 self.min_val = self.data[0]
#                 for i in range(1,len(self.data)):
#                     self.min_val = min(self.min_val,self.data[i])
#
#             return ret
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         if self.data != []:
#             return self.data[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min_val
################################################################################3
class MinStack_v1:
    # 网上的一个方案是额外维护一个栈专门存最小值，能实现的关键条件是数据本身也用栈
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)

        if self.min == []:
            self.min.append(x)
        elif x <= self.min[-1]:#这里有个关键点：等于的情况，涉及出栈的操作，所以同样等于最小值的时候也要入栈
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.data != []:
            ret =  self.data.pop()
            if ret <= self.min[-1]:
                self.min.pop()

            return ret

    def top(self):
        """
        :rtype: int
        """
        if self.data != []:
            return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
#维护最小栈也有两种方案.这种方案是同步维护min的，同步pop，共同进退
class MinStack:
    #
    def __init__(self):
        self.data = []
        self.min = []

    def push(self, x):
        self.data.append(x)
        if self.min == []:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)
        elif x > self.min[-1]:
            self.min.append(self.min[-1])

    def pop(self):
        if self.data != []:
            ret =  self.data.pop()
            self.min.pop()
            return ret

    def top(self):
        if self.data != []:
            return self.data[-1]

    def getMin(self):
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# a = []
# print(a is None)


minStack = MinStack();
minStack.push(-1);
minStack.push(1);
minStack.push(0);
print(minStack.getMin())   #--> 返回 -3.
print(minStack.pop())
print(minStack.top())      #--> 返回 0.
print(minStack.getMin())   #--> 返回 -2.