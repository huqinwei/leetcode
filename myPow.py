#   Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25


class Solution:
    # def myPow(self, x, n):普通方法超时。
    #     """
    #     :type x: float
    #     :type n: int
    #     :rtype: float
    #     """
    #     if n < 0:
    #         n = -n
    #         x = 1 / x
    #     x_origin = x
    #     # print('n:',n)
    #     # print('x:',x)
    #     if n == 0:
    #         return 1
    #     while n-1:
    #         x *= x_origin
    #         n-=1
    #     return x

    # 如果真要二分查找，我又没那些数值，那就拿自然数二分查找？关键是，范围怎么定，移动策略？
    # x不超过100，x的n次，应该就有一个位数的限制，但是n正负也不一样。
    # 但是n是32位，99的n次怎么存的下？
    # x还有负数，x还会正负来回跳的吧。这倒不难，自己看一下n，最后给一下符号就完了



    # 原来二分是说乘法过程二分？
    def myPow(self, x, n):
        if n < 0:
            x, n = 1/x, -n
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 == 0:
            return self.myPow(x*x, n//2)
        else:
            return self.myPow(x*x, n//2) * x


s = Solution()
print("ret:",s.myPow(2.00000,-2))








