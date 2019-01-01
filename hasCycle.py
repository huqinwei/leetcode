#   环形链表
# 给定一个链表，判断链表中是否有环。
#
# 进阶：
# 你能否不使用额外空间解决此题？

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle_slow(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        points = set()
        while head:
            print(id(head))
            if head in points:
                return True
            points.add(head)
            head = head.next
        return False


    def hasCycle(self, head):

        slow_node = head
        fast_node = head
        while slow_node is not None and fast_node is not None:
            slow_node = slow_node.next
            if fast_node.next is not None:
                fast_node = fast_node.next.next
            else:
                return False
            if slow_node == fast_node:
                return True
        return False

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None:
            return False
        slow = head
        fast = head.next
        while slow!=fast:
            if fast==None or fast.next==None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(3)
p4 = ListNode(2)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p1
head = p1



s = Solution()
print(s.hasCycle(p1))

#
# while p1 != None:
#     print(p1.val)
#     p1 = p1.next




