# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


class Solution:
    def climbStairs_myself(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = n * [0]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]#这是错位的，n对应n-1，因为0下标占了一个，也可以从1下标开始


    def climbStairs(self, n):
        dp = (n+3) * [0]#他这个写法，反而能达到简洁的效果
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]



n = 2
sol = Solution()
print('ret:',sol.climbStairs(n))








