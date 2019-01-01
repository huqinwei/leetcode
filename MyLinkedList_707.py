# 设计链表
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val
# 和
# next。val
# 是当前节点的值，next
# 是指向下一个节点的指针 / 引用。如果要使用双向链表，则还需要一个属性
# prev
# 以指示链表中的上一个节点。假设链表中的所有节点都是
# 0 - index
# 的。
#
# 在链表类中实现这些功能：
#
# get(index)：获取链表中第
# index
# 个节点的值。如果索引无效，则返回 - 1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为
# val
# 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为
# val
# 的节点追加到链表的最后一个元素。
# addAtIndex(index, val)：在链表中的第
# index
# 个节点之前添加值为
# val
# 的节点。如果
# index
# 等于链表的长度，则该节点将附加到链表的末尾。如果
# index
# 大于链表长度，则不会插入节点。
# deleteAtIndex(index)：如果索引
# index
# 有效，则删除链表中的第
# index
# 个节点。
#
#
# 示例：
#
# MyLinkedList
# linkedList = new
# MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2); // 链表变为1-> 2-> 3
# linkedList.get(1); // 返回2
# linkedList.deleteAtIndex(1); // 现在链表是1-> 3
# linkedList.get(1); // 返回3
#
# 提示：
#
# 所有值都在[1, 1000]
# 之内。
# 操作次数将在[1, 1000]
# 之内。
# 请不要使用内置的
# LinkedList
# 库。
class linkNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None

# 我用单链表加head、tail指针实现的。
# 感觉做繁琐了，tail指针的维护处处要考虑，双链表更方便点。
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.head = linkNode()
        self.tail = None
        # print(self.head.val)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        # print('index:',index)
        p = self.head
        while index and p:
            p = p.next
            index -= 1
        # print('after,index:',index)
        if index:
            return -1
        if p and p.next:
            return p.next.val
        return -1
        # self.printList()

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        cur = linkNode(val)
        cur.next = self.head.next
        self.head.next = cur

        if cur.next == None:#first node
            self.tail = cur
        # self.printList()

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur = linkNode(val)
        if self.tail == None:#first node
            self.head.next = cur
            self.tail = cur
        else:
            self.tail.next = cur
            self.tail = cur#update tail
        # self.printList()


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0:
            return -1

        p = self.head
        while index and p:#0-index   before index-th
            p = p.next
            index -= 1

        if p == None:
            return
        cur = linkNode(val)
        cur.next = p.next
        p.next = cur
        if cur.next == None:#tail
            self.tail = cur
        # self.printList()

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """

        if index < 0:
            return -1

        p = self.head
        while index and p:#0-index   before index-th
            p = p.next
            index -= 1

        if p == None or p.next == None:
            return
        p.next = p.next.next
        if p.next == None:#注意tail的维护，不是一定要变的，删尾部才要变
            self.tail = p
        # self.printList()
    def printList(self):
        p = self.head
        if p.next == None:
            return
        p = p.next
        i = 0
        str = ''
        while p:

            str += 'node[{0}]:{1}--->'.format(i,p.val)
            p = p.next
            i += 1
        print(str)
        print('tail val:',self.tail.val)

# ["addAtHead","addAtHead","addAtHead",
# [[7],[2],[1],
# "addAtIndex","deleteAtIndex",
# [3,0],[2],
# "addAtHead","addAtTail",
# [6],[4],
# "get","addAtHead","addAtIndex","addAtHead"]
# [4],[4],[5,0],[6]]
# Your MyLinkedList object will be instantiated and called as such:


obj = MyLinkedList()

obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
print('will add 0')
obj.addAtIndex(3,0)
print('will del [3]')
obj.deleteAtIndex(3)
obj.addAtHead(6)
obj.addAtTail(4)
#
#
print(obj.get(4))









def call_function(list1,list2):
    for i in range(len(list1)):
        print(list1[i])
        list1[i](list2[i])
# call_function(["MyLinkedList","addAtHead","get","addAtHead","addAtTail","get","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtIndex","addAtIndex","get","get","addAtIndex","get","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtIndex","addAtIndex","addAtHead","get","deleteAtIndex","addAtIndex","get","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","addAtHead","addAtTail","addAtTail","addAtIndex","get","get","addAtHead","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get","addAtIndex","addAtTail","addAtHead","addAtTail","addAtHead","get","addAtTail","addAtTail","addAtHead","get","get","addAtHead","addAtHead","addAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","addAtIndex","addAtTail","addAtIndex","get","addAtIndex","addAtIndex","get","addAtTail","addAtTail","addAtHead","addAtHead","addAtHead","deleteAtIndex","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","addAtHead","addAtHead","addAtTail","addAtTail","addAtIndex","get","addAtTail","addAtHead","addAtTail","addAtHead"],
# [[],[56],[1],[41],[98],[3],[1,33],[72],[52],[89],[0],[98],[7,97],[2,51],[1],[6],[6,49],[8],[72],[7,8],[8,58],[10],[3,6],[9,61],[63],[16],[7],[16,55],[4],[10],[6],[96],[69],[20],[3],[44],[4],[8,16],[15],[21],[41],[1],[11],[21],[22],[2],[5,7],[62],[95],[91],[69],[24],[51],[94],[93],[29],[10],[68],[13],[32,42],[48],[55],[79],[5],[36],[32],[25,40],[8],[68],[30],[66],[92],[27,26],[90],[11,19],[68],[17,62],[15],[17,97],[35,89],[44],[90],[67],[2],[51],[30],[38],[30],[43],[76],[16],[38],[82],[81],[67],[67],[3,16],[57],[94],[11],[31],[50]])
