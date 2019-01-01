

class Stack():
    def __init__(self,size):
        self.size = size
        self.stack=[]
        self.top = -1

    def push(self,x):
        if self.isfull():
            return -1
        else:
            self.stack.append(x)
            self.top = self.top + 1

    def pop(self):
        if self.isempty():
            return -1
        else:
            self.top = self.top - 1
            self.stack.pop()

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == -1

    def showStack(self):
        print(self.stack)

    def peek(self):
        if self.top != -1:
            return self.stack[-1]
        else:
            return None


s = Stack(10)
for i in range(6):
    s.push(i)
print('peek:',s.peek())
s.showStack()

for i in range(6):
    ret = s.push(i)
    print('ret:',ret)
print('peek:',s.peek())
s.showStack()

for i in range(12):
    ret = s.pop()
    print('ret:',ret)
print('peek:',s.peek())
s.showStack()



# 下边方法是用结构体实现，不借助list
# 顺序是反向的，栈顶逐个指向栈低
##############################################
# #给一个点，我们能够根据这个点知道一些内容
# class Node(object):
#     def __init__(self): #定位的点的值和一个指向
#         self.val=val    #指向元素的值,原队列第二元素
#         self.next=None   #指向的指针
# class stack(object):
#     def __init__(self):
#         self.top=None #初始化最开始的位置
#     def peek(self):  #获取栈顶的元素
#         if self.top!=None:  #如果栈顶不为空
#             return self.top.val  #返回栈顶元素的值
#         else:
#             return None
#     def push(self,n):#添加到栈中
#         n=Node(n)  #实例化节点
#         n.next=self.top  #顶端元素传值给一个指针
#         self.top=n    #
#         return n.val
#     def pop(self):  #退出栈
#         if self.top == None:
#             return None
#         else:
#             tmp=self.top.val
#             self.top=self.top.next  #下移一位，进行
#             return tmp
#
#
# if __name__=="__main__":
#     s=stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#
#     print s.pop()
#     print s.pop()
#     print s.pop()



# l = [1,2,3,4,6,6,6,6,6,6,6]
# print(l)
# l.pop()
# print(l)
# l.pop(0)
# print(l)
# l.pop(1)
# print(l)



#include <iostream>

# class MyQueue {
#     private:
#         // store elements
#         vector<int> data;
#         // a pointer to indicate the start position
#         int p_start;
#     public:
#         MyQueue() {p_start = 0;}
#         /** Insert an element into the queue. Return true if the operation is successful. */
#         bool enQueue(int x) {
#             data.push_back(x);
#             return true;
#         }
#         /** Delete an element from the queue. Return true if the operation is successful. */
#         bool deQueue() {
#             if (isEmpty()) {
#                 return false;
#             }
#             p_start++;
#             return true;
#         };
#         /** Get the front item from the queue. */
#         int Front() {
#             return data[p_start];
#         };
#         /** Checks whether the queue is empty or not. */
#         bool isEmpty()  {
#             return p_start >= data.size();
#         }
# };
#
# int main() {
#     MyQueue q;
#     q.enQueue(5);
#     q.enQueue(3);
#     if (!q.isEmpty()) {
#         cout << q.Front() << endl;
#     }
#     q.deQueue();
#     if (!q.isEmpty()) {
#         cout << q.Front() << endl;
#     }
#     q.deQueue();
#     if (!q.isEmpty()) {
#         cout << q.Front() << endl;
#     }
# }