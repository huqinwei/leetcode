
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # count = 0
        l_ret = ListNode(0)
        l3 = l_ret
        # print('ret:', id(l_ret))
        # print('l3:', id(l3))
        carry = 0
        while True:
            if l1 != None:
                l3.val += l1.val
            if l2 != None:
                l3.val += l2.val
            l3.val += carry

            # if l3.val == 0:
            #     return

            if l3.val // 10 != 0:
                carry = 1
            else:
                carry = 0

            l3.val = l3.val % 10
            print('l3.val:',l3.val)

            # print('p2')
            print('l1:',l1)
            print('l2:',l2)
            print('carry:',carry)

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            if l1 == None and l2 == None and carry == 0:
                print('ret')
                l3.next = None
                return l_ret
            else:
                next_node = ListNode(0)
                l3.next = next_node
                l3 = next_node
            # count += 1
            # if count == 4:
            #     return


print(9 // 10)


l1 = ListNode(1)
l2 = ListNode(8)
# l3 = ListNode(6)

l1.next = l2
l2.next = None
# l3.next = None

l21 = ListNode(0)
# l22 = ListNode(4)
# l23 = ListNode(3)

l21.next = None
# l22.next = l23
# l23.next = None

# print(l1.next)
# print(l2.next)
# print(l2.next.val)
# print(l3.val)
# print(l3.next)

s1 = Solution()
l3 = s1.addTwoNumbers(l1,l21)
print(l3.val)
print(l3.next.val)
if(l3.next.next != None):
    print(l3.next.next.val)
# if(l3.next.next.next != None):
#     print(l3.next.next.next.val)