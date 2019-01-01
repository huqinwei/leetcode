#  颠倒整数
# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。


class Solution:
    def reverse_myself(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = -x
            negative = True
        ret = 0
        while x:
            a = x % 10
            ret += a
            x = x // 10
            if x:
                ret *= 10
            print('x is :',x,' ret is ',ret)
        if ret > 2**31 - 1:
            ret = 0
        return -ret if negative else ret
    def reverse(self, x):

        negative = False
        if x < 0:
            x = -x
            negative = True
        ret = 0
        while x:
            ret *= 10
            a = x % 10
            ret += a
            x = x // 10
            print('x is :',x,' ret is ',ret)
        if ret > 2**31 - 1:
            ret = 0
        return -ret if negative else ret


s1 = Solution()
ret = s1.reverse(123)
print('ret:',ret)





