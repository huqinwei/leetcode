# 奇偶链表
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
# 说明:
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList_myself(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head

        p2 = head2 = head.next
        p1 = head
        while p2 and p2.next:# 一个奇数指针，一个偶数指针，每次跳两格，必须要同步进行，不然会影响另一方
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next

        p1.next = head2
        return head

    def oddEvenList(self, head):
        # 别人的头部处理，只处理空链表，其他都能进循环
        if head == None:
            return head

        odd = oddHead = head
        even = evenHead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead

        return oddHead



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
l = l1
while l != None:
    print(l.val)
    l = l.next




s = Solution()

ret = s.oddEvenList(l1)


l = l1
while l != None:
    print('after:',l.val)
    l = l.next