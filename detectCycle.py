#   环形链表 II
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
# 你是否可以不用额外空间解决此题？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
# 不是随便做一下快满指针，找到碰撞点，是入环的第一个点




p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(1)
p4 = ListNode(9)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p2
head = p1



s = Solution()
node = s.detectCycle(p1)
if node:
    print('ret:',node.val)
else:
    while head != None:
        print(head.val)
        head = head.next

