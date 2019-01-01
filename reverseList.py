
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList_myself(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = p = n = head

        if pre:
            if pre.next:
                if pre.next.next:#3 node:init
                    pre = head
                    p = pre.next
                    n = p.next
                else:#2 node return
                    p = pre.next
                    p.next = pre
                    pre.next = None
                    return p
            else:#1 node return
                return p
        else:
            return []

        pre.next = None#init tail
        while p:
            p.next = pre
            pre = p
            if n:
                p = n
                n = n.next
            else:
                return p
    def reverList_v2(self,head):
        #更简洁的写法
        pre = None
        next = head
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    def reverseList(self,head):#头插法，不断把尾部节点给最头部,cur自己不动，处理的都是cur.next
        if not head:
            return None
        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            tmp.next = head
            head = tmp
        return head



    def reverseList_other(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        n = head.next
        cur.next = None
        while n is not None:
            r = n.next
            n.next = cur
            cur = n
            n = r
        return cur


p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(1)
p4 = ListNode(9)
p1.next = p2
p2.next = p3
p3.next = p4
head = p1



s = Solution()
new_head = s.reverseList(p1)


while new_head != None:
    print(new_head.val)
    new_head = new_head.next




#########################################################################
###################################################################################
#做链表逆序
#@这个不叫头插法？甩尾叫做就地逆置#!!!!!!!!!!!!!!!!!!!!!!!

class listNode:
    def __init__(self,val):
        self.val = val
        self.next = None

l1 = listNode(1)
l2 = listNode(2)
l3 = listNode(3)
l4 = listNode(4)
l5 = listNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
head = l1
while head:
    print(head.val)
    head = head.next


# def reverseListNode(head):
#     new_head = None
#     if not head:
#         return None
#     next = head.next
#     while head:
#         head.next = new_head
#         new_head = head
#         head = next
#         if next:
#             next = next.next
# return new_head

def reverseListNode(head):
    new_head = None
    if not head:
        return None
    while head:
        next = head.next##优化，这样就不用多余判定了
        head.next = new_head
        new_head = head
        head = next
    return new_head

# #用头插法做链表逆序
# 感觉没有本质区别，头插法就是做一个临时头节点，插在它的后边。
# 确实有不同，这算在一个“固定位置”不停的插入吧，那个算甩尾吧。论最终结果，那肯定得一样啊。
def reverseListNode_headInsert(head):
    temp_head = listNode(0)
    if not head:
        return None
    while head:
        next = head.next##优化，这样就不用多余判定了
        head.next = temp_head.next
        temp_head.next = head
        head = next
    return temp_head.next


ret = reverseListNode_headInsert(l1)
while ret:
    print('reversed:',ret.val)
    ret = ret.next


print(reverseListNode(None))












