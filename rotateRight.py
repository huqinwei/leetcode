#  旋转链表
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight_myself(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        p = head
        n = 0
        while p and p.next:
            p = p.next
            n += 1
        p.next = head
        n += 1
        # print('count:',n)

        k = k % n
        k = n - k#因为是向右移动k,所以是向左移动n-k
        while k:
            head = head.next
            k -= 1
        tail = head
        while n-1:
            tail = tail.next
            n -= 1
        tail.next = None

        # p = head
        # while p != None:
        #     print(p.val)
        #     p = p.next
        return head

    #总的来说比我的简洁一些，尤其是那个互补操作
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        p_fast = head
        p_slow = head
        cnt = 0
        while p_fast:
            cnt += 1
            p_fast = p_fast.next

        p_fast = head
        k = k % cnt
        for i in range(k):#k-1
            p_fast = p_fast.next

        while p_fast.next:#同样是利用补，右移k等于左移n-k，现在利用已经移动过k-1的fast，使slow移动n-1-(k-1)!!!!
            p_fast = p_fast.next
            p_slow = p_slow.next
        p_fast.next = head#然后再拼接环，再重新分配head，注意slow的下一个才是head，slow就用来断环
        head = p_slow.next
        p_slow.next = None

        return head

l1 = ListNode(5)
l2 = ListNode(6)
l3 = ListNode(9)
l4 = ListNode(19)
l5 = ListNode(29)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l = l1
while l != None:
    print(l.val)
    l = l.next


s = Solution()

ret = s.rotateRight(l1,7)
l = ret
while l != None:
    print('after:',l.val)
    l = l.next




