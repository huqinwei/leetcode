# 二分查找
# 给定一个
# n
# 个元素有序的（升序）整型数组
# nums
# 和一个目标值
# target  ，写一个函数搜索
# nums
# 中的
# target，如果目标值存在返回下标，否则返回 - 1。
#
#

# 示例
# 2:
#
# 输入: nums = [-1, 0, 3, 5, 9, 12], target = 2
# 输出: -1
# 解释: 2
# 不存在
# nums
# 中因此返回 - 1
#
# 提示：
#
# 你可以假设
# nums
# 中的所有元素是不重复的。
# n
# 将在[1, 10000]
# 之间。
# nums
# 的每个元素都将在[-9999, 9999]
# 之间。

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        mid = n // 2
        # print(nums)
        # print('mid:',mid)
        # print('mid:',nums[mid])
        if target > nums[mid]:
            ret = self.search(nums[mid+1:],target)
            if ret == -1:
                return -1
            return ret + mid + 1
        elif target < nums[mid]:
            return self.search(nums[:mid],target)
        else:
            return mid

    def search_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s=0
        e=len(nums)-1
        while s<=e:
            mid=(s+e)//2
            if target>nums[mid]:
                s=mid+1
            elif target<nums[mid]:
                e=mid-1
            else:
                return mid
        return -1


nums = [-1,0,3,5,9,12]
target = 2
# 输出: 4
# 解释: 9


# print(nums[:5])
# print(nums[5:])
s = Solution()
print(s.search(nums,target))












