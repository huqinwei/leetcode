#   删除链表中的节点
# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#
# 现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#
#     4 -> 5 -> 1 -> 9
# 示例 1:
#
# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
# 示例 2:
#
# 输入: head = [4,5,1,9], node = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
# 说明:
#
# 链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 不要从你的函数中返回任何结果。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(1)
p4 = ListNode(9)
p1.next = p2
p2.next = p3
p3.next = p4
head = p1


# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         global head
#         if head.val == node:
#             # print('bingo')
#             cur = head
#             head = head.next
#             del cur
#             return
#         pre = head
#         p = head.next
#         while p != None:
#             if p.val == node:
#                 cur = p
#                 pre.next = p.next
#                 del cur
#                 return
#             p = p.next
#             pre = pre.next
# 理解错题意了，传入的是个节点，就是说外部可能有个链表，给你一个节点指针，让你给跳过去。

class Solution:
    def deleteNode_myself(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur.next != None:
            cur.val = cur.next.val
            if cur.next.next == None:
                tmp = cur.next
                cur.next = None
                del tmp
                break
            cur = cur.next

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        tmp = node.next
        node.next = node.next.next
        del tmp




s = Solution()
s.deleteNode(p3)

p = head
while p != None:
    print(p.val)
    p = p.next

