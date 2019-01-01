# 53. 最大子序和
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6

# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 他说起来简单，其实难在怎么找到这个关系，而不在于怎么设计这个dp，dp是为关系服务的。
# 你找到了前边N个总数是负的，那么这一段可以舍弃的关键点，知道这个方法可行，才能想出来dp怎么实现


class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if 0 == n:
            return 0
        dp = n * [0]
        dp[0] = nums[0]
        max_len = dp[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i],nums[i])#把dp[i-1]看做一个整体，是负数则抛弃
            max_len = max(dp[i],max_len)

        return max_len

sol = Solution()
print('ret:',sol.maxSubArray(nums))




