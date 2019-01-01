# def binarySearch(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     if len(nums) == 0:
#         return -1
#
#     left, right = 0, len(nums)
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#
#     # Post-processing:
#     # End Condition: left == right
#     if left != len(nums) and nums[left] == target:
#         return left
#     return -1

#   寻找峰值
# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。


class Solution:
    # def findPeakElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     left = 0
    #     right = len(nums)
    #     while left < right:
    #
    #         # if left < 0:
    #         #     l_value = -2**31
    #         # else:
    #         #     l_value = nums[left]
    #         if right >= len(nums):
    #             r_value = -2**31
    #         else:
    #             r_value = nums[right]
    #
    #         mid = (left + right) // 2
    #         if nums[left] >= r_value and nums[left] >= nums[mid]:
    #             right = mid
    #         elif r_value >= nums[left] and r_value >= nums[mid]:
    #             left = mid + 1
    #         elif nums[mid] > nums[left] and nums[mid] > r_value:
    #             right = mid
    #         elif nums[mid] < nums[left] and nums[mid] < r_value:
    #             #whatever
    #             print("condition4")
    #             right = mid
    #
    #     return right
        # 这样不对，这样只是找一段中的极点，mid是比left和right都大，你无法保证mid右边就比mid小，所以不能这样向右靠拢
        # mid自身的前后都要比较，如果mid就是个波峰，就能返回，如果不是。向增长的方向靠。。。


    def findPeakElement_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:

            mid = (left + right) // 2
            if mid - 1 < 0:
                l_value = -2**31
            else:
                l_value = nums[mid-1]
            if mid + 1 >= len(nums):
                r_value = -2**31
            else:
                r_value = nums[mid+1]
            # print('l_value:',l_value)
            # print('r_value:',r_value)
            # print('nums[',mid,']:',nums[mid])
            # 为了保证是波峰，比较的不是left和right，而是mid前后1，又因为他案例可以是一个最小值，或者两个，分别是最小和倒数第二小，所以多做了很多处理
            if nums[mid] > l_value and nums[mid] > r_value:
                return mid
            elif nums[mid] > l_value:
                left = mid + 1
            elif nums[mid] > r_value:
                right = mid
            elif nums[mid] < l_value:
                right = mid
            else:#nums = [-2147483648]#大前提，没有两个相邻的相等，不然过不去:[1,2,3,3]
                return mid
        return right

    # 这个土法子居然更快？并没有，系统的时间不一致。。。
    def findPeakElement_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = 0
        for i in range(len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        return max_index

    # 另一个各种比较的例子
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l = len(nums)
        if l == 1:
            return 0

        left,right = 0,l-1

        while True:

            if right - left == 1:
                if nums[left] > nums[right]:
                    return left
                return right

            mid = left + (right-left) // 2

            if nums[left] > nums[left+1]:
                return left

            if nums[right] > nums[right-1]:
                return right

            if nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]:
                return mid

            if nums[mid] < nums[mid+1] and nums[mid-1] < nums[mid]:
                left = mid
            else:
                right = mid

nums = [-2147483648,-2147483647]
s = Solution()
print(s.findPeakElement(nums))


a = -2**31
print(a)

