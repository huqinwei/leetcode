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


#   第一个错误的版本
# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。
#
# 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
#
# 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
#
# 示例:
#
# 给定 n = 5，并且 version = 4 是第一个错误的版本。
#
# 调用 isBadVersion(3) -> false
# 调用 isBadVersion(5) -> true
# 调用 isBadVersion(4) -> true
#
# 所以，4 是第一个错误的版本。


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
bad_begin = 4
def isBadVersion(version):
    global bad_begin
    if version >= bad_begin:
        return True
    return False
print(isBadVersion(5))
print(isBadVersion(4))
print(isBadVersion(3))

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1
        left = 1
        right = n + 1
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):#mid >= target
                right = mid
            else:
                left = mid + 1
        # print('left:',left)
        return left



n = 15
s = Solution()
print(s.firstBadVersion(n))

