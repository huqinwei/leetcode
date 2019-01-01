#   移除链表元素
# 删除链表中等于给定值 val 的所有节点。
#
# 示例:
#
# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = head
        if not p:
            return None
        while p and p.val == val:#preprocessing
            p = p.next
        head = p


        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head

l1 = ListNode(5)
l2 = ListNode(6)
l3 = ListNode(9)
l1.next = l2
l2.next = l3
l = l1
while l != None:
    print(l.val)
    l = l.next



s = Solution()

ret = s.removeElements(l1,6)


l = l1
while l != None:
    print('l:',l.val)
    l = l.next

while ret != None:
    print('ret:',ret.val)
    ret = ret.next