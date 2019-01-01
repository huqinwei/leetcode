#   二进制求和
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"

class Solution:
    def addBinary_myself(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list1 = list(a)
        list2 = list(b)
        n1 = len(list1)
        n2 = len(list2)
        i = n1 - 1
        j = n2 - 1
        carry = 0
        ret = ''
        while i >= 0 or j >= 0:
            cur = 0
            cur += carry
            if i >= 0:
                cur += int(list1[i])
                i -= 1
            if j >= 0:
                cur += int(list2[j])
                j -= 1
            print('cur',cur)
            if cur > 1:
                carry = 1
            else:
                carry = 0
            if cur % 2 == 1:
                ret = '1' + ret
            else:
                ret = '0' + ret
        if carry:
            ret = '1' + ret

        return ret
    def addBinary(self, a, b):

        n1 = len(a)
        n2 = len(b)
        i = n1 - 1
        j = n2 - 1
        carry = 0
        ret = ''
        while i >= 0 or j >= 0:
            cur = 0
            cur += carry
            if i >= 0:
                cur += int(a[i])
                i -= 1
            if j >= 0:
                cur += int(b[j])
                j -= 1
            print('cur',cur)
            if cur > 1:
                carry = 1
            else:
                carry = 0
            if cur % 2 == 1:
                ret = '1' + ret
            else:
                ret = '0' + ret
        if carry:
            ret = '1' + ret

        return ret



    def addBinary_other(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = int(a, 2), int(b, 2)
        return bin(a + b)[2:]
a = "1010"
b = "1011"
s = Solution()
# print('ret:',s.addBinary(a,b))

a_int = int(a,2)
b_int = int(b,2)
print(a_int)
print(b_int)
print(type(a_int))
print(a_int+b_int)
print(bin(a_int+b_int))
print(bin(a_int+b_int)[2:])
# print((a_int+b_int)[2:])



# str1 = 'hello'
# for i in str1:
#     print(i)
# p = str1[0]
# list1 = list(str1)
# n = len(list1)
# i = 0
# while i < n:
#     print(list1[i])
#     i += 1





