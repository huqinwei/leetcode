# 有效的完全平方数
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
# 输入：16
# 输出：True

# 示例 2：
# 输入：14
# 输出：False


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left = 1
        right = num // 2 + 1
        while left + 1 < right:
            mid = (left + right) // 2
            # print('left:',left,' right:',right,' mid:',mid)
            if mid * mid == num:
                return True
            if mid * mid < num:
                left = mid
            else:
                right = mid

        return False


s = Solution()
print('ret:',s.isPerfectSquare(14))







