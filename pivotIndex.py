# 寻找数组的中心索引
# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
#
# 示例 1:
#
# 输入:
# nums = [1, 7, 3, 6, 5, 6]
# 输出: 3
# 解释:
# 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
# 同时, 3 也是第一个符合要求的中心索引。
# 示例 2:
#
# 输入:
# nums = [1, 2, 3]
# 输出: -1
# 解释:
# 数组中不存在满足此条件的中心索引。
# 说明:
#
# nums 的长度范围为 [0, 10000]。
# 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。



# 很麻烦啊，负数也要处理，但是又不能保证全是负数，所以也不能你是0，他是-10，就你这边移动。
# 你这边移动，可能是越来越大的正数，他那边移动，可能是越来越小的负数，总之，双指针对比sum不妥
class Solution:
    # def pivotIndex_failed(self, nums):#不考虑负数的
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n < 3:
    #         if n == 2 and nums[1] == 0:
    #             return 0
    #         if n == 2 and nums[0] == 0:
    #             return 1
    #         if n == 1:
    #             return 0
    #         return -1
    #     l = 0
    #     r = len(nums)-1
    #     l_sum = nums[l]
    #     r_sum = nums[r]
    #     index = -1
    #     while l < r - 1:
    #         print('l:',l,' r:',r)
    #         if l_sum < r_sum:
    #             l += 1
    #             if l == r - 1:
    #                 index = l
    #                 break
    #             l_sum += nums[l]
    #
    #         else:
    #             r -= 1
    #             if r == l + 1:
    #                 index = r
    #                 break
    #             r_sum += nums[r]
    #     if l_sum != r_sum:
    #         return -1
    #     return index

# 提示也只是try遍历两次解决问题，看来应该可以用更宽松的方法完成
#     We    can    precompute    prefix    sums    P[i] = nums[0] + nums[1] + ... + nums[i - 1].Then
#     for each index, the left sum is P[i], and the right sum is P[P.length - 1] - P[i] - nums[i].
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left_sums = [0]*(n+1)
        sum = 0
        for i in range(0,n):
            left_sums[i] = sum
            sum += nums[i]
        left_sums[n] = sum
        print(left_sums)
        for i in range(n):
            # print('===================i:',i)
            # print(left_sums[i])
            # print(left_sums[n])
            # print(left_sums[i+1])
            if left_sums[i] == left_sums[n] - left_sums[i+1]:
                return i
        return -1

    # 这个看起来效率还要高
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1,sum2=0,sum(nums)
        for i in range(len(nums)):
            sum2-=nums[i]
            if sum1==sum2:
                return i
            sum1+=nums[i]
        return -1

nums = [1, 7, 3, 6, 5, 6]
# nums = [1,2,3]
# nums = [0,0]
# nums = [-1,-1,-1,-1,-1,0]
nums = [-1,-1,0,1,1,0]
print(nums)
s = Solution()
print('ret:',s.pivotIndex(nums))







