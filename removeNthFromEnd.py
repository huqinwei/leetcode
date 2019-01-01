#   删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 想一遍遍历解决问题，只能用list存下所有的指针，然后计算出用哪个指针。
    def removeNthFromEnd_myself(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        points = []
        p = head
        while p:
            points.append(p)
            p = p.next
            # print(points)
        size = len(points)
        if n == 1:
            if size > 1:
                p = points[-2]
                # todel = p.next
                p.next = None
                # del todel#没有这方面的要求，省略
            else:
                del head
                return None
        else:
            cur = points[-n]
            # print('cur val:',cur.val)
            cur.val = cur.next.val
            # todel = cur.next
            cur.next = cur.next.next
            # del todel#没有这方面的要求，省略
        return head

    # 别人的
    # def removeNthFromEnd(self, head, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     """
    #     i=0
    #     delprep=end=head
    #     #find the nth element
    #     while end!=None:
    #         end=end.next
    #         if i>n:
    #             delprep=delprep.next#i比n多出来的部分，都导致这个delprep迭代，i是总长，n是倒数第几，所以等于求出i-n
    #         i+=1#不过这个计数方法确实挺特别
    #         print('i:',i)
    #     #delete the nth element
    #     if i<=n:#头结点特殊处理
    #         dele=head
    #         head=dele.next
    #     else:#常规，就是拿那个指针去删一下
    #         dele=delprep.next
    #         delprep.next=dele.next
    #     return head


    # def removeNthFromEnd_bad(self, head, n):#这个方法的fast和slow关系不好
    #
    #     if not head or n < 1:
    #         return head
    #     slow = fast = head
    #     while n:#你不知道链表总长度，不能提前处理n超长的情况，只能自己评估
    #         if fast:
    #             fast = fast.next
    #         else:
    #             break
    #         n -= 1
    #     if n > 0:
    #         return head
    #
    #     while fast:
    #         fast = fast.next
    #         slow = slow.next
    #     if slow.next:#不能用替换当前指针的值，删除下一个节点的方法，因为slow到了最后,倒数第一个删不掉
    #         slow .val = slow.next.val
    #         slow.next = slow.next.next
    #     return head

    # 别人的做法，核心思维是快慢指针：一个指针移动n，两个指针绑定移动，直到最后，第二个指针移动的就是size-n，就找到了倒数n
    def removeNthFromEnd_v1(self, head, n):
        # 这个方法一致性太差了。。。。。第一遍fast可以到non，第二遍不可以
        if not head or n < 1:
            return head
        slow = fast = head
        for _ in range(n):#你不知道链表总长度，不能提前处理n超长的情况，只能自己评估
            if not fast:#这个才是关键截停点，这个丢了，逻辑怎么都不通
                return None#如果不return，说明至少是够长的，
            fast = fast.next
        if not fast:#处理边界问题
            return head.next

        # 这个也是间接利用了size-n，fast已经移动了n步，fast和slow同步移动，fast停止就是size-n
        while fast.next:#slow还是要起pre的作用，所以fast也是不能出格，前边的循环就出格了，只不过那个情况特殊处理了，总之，一致性太差，这个方法不值得记忆
            fast = fast.next
            slow = slow.next

        # if slow.next:因为fast不出格，slow比fast小，所以slow.next不用判断都有
        slow.next = slow.next.next

        return head

    #个人基于前边一版做的优化,加了个爸爸，改善了一致性.slow比fast又慢了一步，slow干脆叫pre
    def removeNthFromEnd_myself2(self, head, n):
        father = ListNode(0)
        father.next = head
        pre = father

        if not head or n < 1:
            return head
        fast = head
        for _ in range(n):
            if not fast:#这个才是关键截停点，这个丢了，逻辑怎么都不通
                return None#如果不return，说明至少是够长的，
            fast = fast.next
        if not fast:#处理边界问题
            return head.next

        # 这个也是间接利用了size-n，fast已经移动了n步，fast和slow同步移动，fast停止就是size-n
        while fast:#slow还是要起pre的作用，所以fast也是不能出格，前边的循环就出格了，只不过那个情况特殊处理了，总之，一致性太差，这个方法不值得记忆
            fast = fast.next
            pre = pre.next

        pre.next = pre.next.next

        return head

    # 这是土法子，a是全长，遍历之后再来一遍
    def removeNthFromEnd_other(self, head, n):
        if head == None:
            return None
        if head.next == None and n==1:
            return None
        if head.next == None and n==0:#他把1个以内的长度特殊处理了
            return head
        cur = head
        a = 1
        while cur.next != None:
            a += 1
            cur = cur.next
        b = a - n
        cur = head
        c = 1
        if b == 0:
            return head.next
        while c != b:
            cur = cur.next
            c += 1
        cur.next = cur.next.next
        return head
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4
head = p1



s = Solution()
new_head = s.removeNthFromEnd(p1,2)


while new_head != None:
    print(new_head.val)
    new_head = new_head.next





