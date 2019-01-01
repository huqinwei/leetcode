# 合并
# k
# 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

    def mergeKLists_myself(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodes = []
        for i in range(len(lists)):
            p = lists[i]
            while p:
                nodes.append([p.val,p])
                p = p.next
        nodes.sort(key=lambda nodes:nodes[0])
        pre = new_head = ListNode(0)

        for p in nodes:
            # print(p[1].val)
            pre.next = p[1]
            pre = p[1]
        return new_head.next

    #这人直接复制了一份
    def mergeKLists_copy(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        total=[]
        tmp=result=ListNode(0)
        for L in lists:
            while L:
                total.append(L.val)
                L=L.next
        total.sort()
        for i in range(len(total)):
            tmp.next=ListNode(total[i])
            tmp=tmp.next
        tmp.next=None
        return result.next

    def mergeKLists(self, lists):
        n = len(lists)
        if not n:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return self.mergeTwoLists(lists[0],lists[1])

        mid = len(lists) // 2
        sub_lists1 = []
        sub_lists2 = []

        for i in range(0,mid):
            sub_lists1.append(lists[i])
        for i in range(mid,len(lists)):
            sub_lists2.append(lists[i])

        l1 = self.mergeKLists(sub_lists1)
        l2 = self.mergeKLists(sub_lists2)

        return self.mergeTwoLists(l1,l2)



l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(5)
l1.next = l2
l2.next = l3
l21 = ListNode(1)
l22 = ListNode(3)
l23 = ListNode(4)
l21.next = l22
l22.next = l23
l31 = ListNode(2)
l32 = ListNode(6)
l31.next = l32
lists=[l1,l21,l31]

# 输出: 1->1->2->3->4->4->5->6
s = Solution()
root = s.mergeKLists(lists)
while root:
    print(root.val)
    root = root.next