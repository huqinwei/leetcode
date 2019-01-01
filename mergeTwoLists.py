# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 三循环：总复杂度还是O(m + n)，只是为了方便写逻辑，l1和l2有一个到头了就停下，然后把多余的一个都插进来
        # if l1 == None and l2 == None:
        #     return []
        # l = ListNode(0)
        # lp = l
        # while l1 != None and l2 != None:
        #     # print('l1.val:{0},l2.val{1}'.format(l1.val,l2.val))
        #     if l1.val < l2.val:
        #         lp.val = l1.val
        #         l1 = l1.next
        #     else:
        #         lp.val = l2.val
        #         l2 = l2.next
        #     l_new = ListNode(0)
        #     lp.next = l_new
        #     lp = l_new
        #
        # # print("l1:{0},l2:{1}".format(l1,l2))
        # while l1 != None:
        #     # print('l1.val:{0}'.format(l1.val))
        #     lp.val = l1.val
        #     l1 = l1.next
        #     if l1 != None:
        #         l_new = ListNode(0)
        #         lp.next = l_new
        #         lp = l_new
        #
        # while l2 != None:
        #     lp.val = l2.val
        #     l2 = l2.next
        #     if l2 != None:
        #         l_new = ListNode(0)
        #         lp.next = l_new
        #         lp = l_new
        # return l
##########################################################################################3
        # 因为是链表，其实多余的部分不用再用循环插了，直接next接上去就行了，这里边也没要求你用独立空间，没说不能用传入数据。这种都太取巧了，实际写程序不能这么写，但是做题可以。
###################################################################################3
        # 这个方法一次用一个旧节点，但是也不新建。
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
        # 我说他第一个节点多余了是怎么处理的，直接用return first.next跳过第一个节点
        # 很多解法都用到了这个技巧，的确，也没要求不浪费，但是这些解法放到实际程序中都很坑吧。果然是做题怪，做完了不会正常思维了。
        # 另外，即使这样，也没提高我的速度，可能跟leetcode系统有关系。


l1 = ListNode(5)
l2 = ListNode(6)
l3 = ListNode(9)
l1.next = l2
l2.next = l3
l = l1
while l != None:
    print(l.val)
    l = l.next


l11 = ListNode(3)
l12 = ListNode(6)
l13 = ListNode(7)
l11.next = l12
l12.next = l13

l = l11
while l != None:
    print(l.val)
    l = l.next

s = Solution()

ret = s.mergeTwoLists(l1,l11)

while ret != None:
    print(ret.val)
    ret = ret.next




