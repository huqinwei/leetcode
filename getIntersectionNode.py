# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
#
#
#
# 例如，下面的两个链表：
#
# A: a1 → a2
# ↘
# c1 → c2 → c3
# ↗
# B: b1 → b2 → b3
# 在节点
# c1
# 开始相交。
#
#
#
# 注意：
#
# 如果两个链表没有交点，返回
# null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足
# O(n)
# 时间复杂度，且仅用
# O(1)
# 内存。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def getIntersectionNode(self, headA, headB):
    #     """
    #     :type head1, head1: ListNode
    #     :rtype: ListNode
    #     """
    # 这其实就是变相的查是不是有环。
    # p1变成headB，p2变成headA，这就是在走逻辑上的环。
    # 假设有环，这个逻辑就能保证最后汇合点还是那个交叉点。
    # 假设没环，这个问题中，没环也就是说两链表不相交。不相交的话，两个链表要么等长，同是None，相等，返回None。
    # 要么不等长，多走一圈，最终同时等于None，这个逻辑是，你长3，他长2，你走3 + 2，他走2 + 3，最后同时走完。
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            # print(p1.val,p2.val)
            p1 = headB if p1 == None else p1.next
            print()
            p2 = headA if p2 == None else p2.next
            print(p1,p2)
        return p1


p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)


p1.next = p2
p2.next = p3


p21 = ListNode(11)
p22 = ListNode(12)
p23 = ListNode(13)
p21.next = p22
# p22.next = p23


s = Solution()
node = s.getIntersectionNode(p1,p21)
if node:
    print(node.val)
else:
    print('none')


while p21 != None:
    print(p21.val)
    p21 = p21.next