# 至少是其他数字两倍的最大数
# 在一个给定的数组nums中，总是存在一个最大元素 。
#
# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
#
# 如果是，则返回最大元素的索引，否则返回 - 1。
#
# 示例
# 1:
#
# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6
# 是最大的整数, 对于数组中的其他整数,
# 6
# 大于数组中其他元素的两倍。6
# 的索引是1, 所以我们返回1.
#
# 示例
# 2:
#
# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4
# 没有超过3的两倍大, 所以我们返回 - 1.
#
# 提示:
#
# nums
# 的长度范围在[1, 50].
# 每个
# nums[i]
# 的整数范围在[0, 99].


class Solution:
    def dominantIndex_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        first_index = -1
        second = 0
        second_index = -1
        for i,v in enumerate(nums):
            if v > second:
                second = v
                second_index = i
            if second > first:
                second,first = first,second
                second_index,first_index = first_index,second_index
            # print(first,second)
            # print(first_index,second_index)
        if first >= second * 2:
            return first_index
        return -1


    def dominantIndex(self, nums):#40ms
        """
        :type nums: List[int]
        :rtype: int
        """
        maxn = max(nums)

        for item in nums:
            if maxn < 2 * item and maxn != item:
                return -1
        return nums.index(maxn)


nums = [0,0,0,1]
s = Solution()
print('ret:',s.dominantIndex(nums))















