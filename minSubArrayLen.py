class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        l = 0
        r = len(nums)-1
        while l <= r:#注意结束条件，l和r相等就结束了，最短长1,不应该存在找到最后都找不到的情况，因为预处理了
            if sum(nums[l+1:r+1]) >= s and sum(nums[l:r]) >= s:
                if nums[l] > nums[r]:#双原则：1，往左移动不影响。2，左边的数更大。。#找的是最小长度，所以优先去掉小的
                    r -= 1
                else:
                    l += 1
            elif sum(nums[l+1:r+1]) >= s:#前提：往右移动不影响
                l += 1
            elif sum(nums[l:r]) >= s:
                r -= 1
            else:#总之，所有移动都是试探性的，要把所有条件都试探过了，最后决定不能移动，而不是直接按着一个大小规则就动起来,比普通双指针难点
                return r - l + 1

n=7
nums = [2,3,1,2,4,3]
nums = [2,3,7,2,4,3]
print(sum(nums))
print(sum(nums[0:5]))

# n = 15
# nums = [5,1,3,5,10,7,4,9,2,8]

# n = 4
# nums=[1,4,4]



s1 = Solution()
ret = s1.minSubArrayLen(n,nums)
print('ret:',ret)


