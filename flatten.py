# 扁平化多级双向链表
# 您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
#
# 扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。
#
#
#
# 示例:
#
# 输入:
# 1 - --2 - --3 - --4 - --5 - --6 - -NULL
# |
# 7 - --8 - --9 - --10 - -NULL
# |
# 11 - -12 - -NULL
#
# 输出:
# 1 - 2 - 3 - 7 - 8 - 11 - 12 - 9 - 10 - 4 - 5 - 6 - NULL\\\\\\\\\


# 看起来就是一个DFS结构，碰到child就先访问child，返回的是平铺后的，两种处理，一种是新return一个链表，逐个加进去，另一个是直接原地修改？


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        p = head
        while p:
            if p.child:
                r = p.next#reserved
                q = p.child
                while q and q.next:
                    q = q.next
                # print('q:',q.val)
                p.child.prev = p
                p.next = p.child
                p.child = None
                q.next = r
                if r:
                    r.prev = q

            p = p.next
        return head
node1 = Node(1,None,None,None)
node2 = Node(2,None,None,None)
node3 = Node(3,None,None,None)
node22 = Node(22,None,None,None)
node23 = Node(23,None,None,None)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node2.child = node22
node22.next = node23
node23.prev = node22

p = node1
while p:
    print('before:',p.val)
    p = p.next
s= Solution()
ret = s.flatten(node1)

p = ret
while p:
    print(p.val)
    p = p.next



