# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        head2 = ListNode(0)
        pre_head = ListNode(0)
        pre_head.next = head
        tail2 = head2
        cur = pre_head
        while cur and cur.next:
            if cur.next.val >= x:
                tail2.next = cur.next
                tail2 = cur.next
                cur.next = cur.next.next
                continue
            # elif cur.next.val == x:#这个题意也是个坑，等于的那一个点不是中点，大于等于同等对待
            cur = cur.next
        tail2.next = None
        cur.next = head2.next

        return pre_head.next#别看pre_head.next是head，后边变了，head自身已经到后边了，所以还是用pre_head.next




p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(1)
p4 = ListNode(9)
p5 = ListNode(3)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
head = p1



s = Solution()
new_head = s.partition(head,2)


while new_head != None:
    print(new_head.val)
    new_head = new_head.next
