# 寻找旋转排序数组中的最小值
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0

# 被专题的模板坑了，其实可能并不适用？
class Solution:
    def findMin_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:#实测这一步确实能加速
                return nums[mid+1]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
    def findMin_v1(self, nums):#和我一样的,没我的对比拦截，按理说更慢,同时提交，确实更慢
        i = 0
        j = len(nums) - 1
        while i < j:
            m = i + (j - i) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]
    def findMin(self, nums):#和我一样的
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0,len(nums)-1
        while low < high:
            if nums[low] < nums[high]:#这个条件和我有所不同，确实也可以用，旋转不可能有其他情况
                return nums[low]

            mid = (low+high)//2
            if nums[mid] >= nums[low]:
                low = mid+1
            else:
                high = mid
        return nums[low]


nums = [4,5,6,7,0,1,2]
nums = [1,2,4,5,6,7,0,]
nums = [0,1,2,4,5,6,7,]
nums = [5,1,2,3,4,]
s = Solution()
print('ret:',s.findMin(nums))






