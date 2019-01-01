class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween_myself(self, head, m, n):
        if m == n:
            return head
        pre_tail = None
        cur = head
        cnt = m
        while cnt>1 and cur:
            cnt -= 1
            pre_tail = cur
            cur = cur.next
        if pre_tail:
            print('pre_tail:',pre_tail.val)
        print('cur:', cur.val)
        pre = None
        new_tail = None
        while cur and n - m + 1:
            print('loop cur:',cur.val)
            next = cur.next
            if not pre:
                new_tail = cur
            cur.next = pre
            pre = cur
            cur = next
            n -= 1
        new_tail.next = next
        if pre_tail:#注意，m和n都是带“等于”的，2就是第二个，1就是第一个，如果从1就开始反转，那么就没有pre_tail
            pre_tail.next = pre
            return head
        else:
            return pre

    def reverseBetween(self, head, m, n):
        def reverseBetween(self, head, m, n):
            """
            :type head: ListNode
            :type m: int
            :type n: int
            :rtype: ListNode
            """
            if head == None:#他先排除了只有一个节点的情况。然后实现双指针p和q
                return head
            elif head.next == None:
                return head

            dummy = ListNode(None)#确实和我想的一样，他在头结点之前也做了一个辅助节点,以此处理第一个点就开始反转的情况
            dummy.next = head
            p = dummy
            q = dummy.next
            for i in range(1, m):
                p = p.next
                q = q.next

            # 好像算头插法？因为题目说了m和n的条件，其实不用多余去判断尾部，但是头部不能忽略，至少我那个方法是
            # p和q都没动
            # 这个操作过程的常态，是一个链环,只是逻辑上的分叉点，其实单链表哪有分叉点？
            # r是分叉点，作为新链表的head，
            for i in range(m, n):
                r = p.next
                p.next = q.next
                q.next = p.next.next#q作为新链表的尾部，主要负责链住原来的尾部。单链表不能分叉，这个点也是能迭代前进的关键。
                p.next.next = r

            return dummy.next#只要return dummy.next就能无差别对待首节点反转

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


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
p2.next = p3
# p3.next = p4
# p4.next = p5
head = p1

s = Solution()
new_head = s.reverseBetween(head,1,2)


while new_head != None:
    print(new_head.val)
    new_head = new_head.next
