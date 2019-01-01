#   回文链表
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？



# 栈的思维，只限于偶数，还不好说有没有特例出问题。这里如果是奇数就没办法了
# 翻转的思路也不行吧，翻转过来你也不能直接对比，这是链表
# 存一个翻转的链表，是O(n)，再遍历对比，还是O(n)，而且空间复杂度也是O(n)
# 没达到他说的境界
# 把读出来的值放到list，然后拿list和reverse后的对比，这个是否可行？但是不知道reverse接口的实现！反正应该是达不到要求了，他说的是O(1)的空间复杂度。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome_myself(self, head):
        l = []
        while head:
            l.append(head.val)

            head = head.next
        l2 = l.copy()#接口的reverse是原地的，需要拷贝，所以空间复杂度乘2
        l.reverse()
        return l == l2
    def isPalindrome_v2(self, head):
        if not head:
            return True
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[::-1]#这个技巧

#################todo@@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = node
            node = curr
        while head and node:
            if head.val != node.val:
                return False
            head = head.next
            node = node.next
        return True



p1 = ListNode(4)
p2 = ListNode(5)
p3 = ListNode(4)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4
head = p1



s = Solution()
print(s.isPalindrome(p1))


while p1 != None:
    print(p1.val)
    p1 = p1.next



l = [1,2,3,4]
print(l)
print(l[::-1])
print(l == l[::-1])








