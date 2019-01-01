# 删除排序数组中的重复项 II
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定 nums = [1,1,1,2,2,3],
#
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,1,2,3,3],
#
# 函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

class Solution:
    def removeDuplicates(self, nums):
        # 只有初始count是0，只要i存住了一个数字，count就是1，存两个同样数字，之后，count大于1，后边的count大于1，j动i不动
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        count = 0
        for j in range(0,n):
            # print('i:{0},j:{1}'.format(i,j))
            # print('nums[i]:{0},nums[j]:{1}'.format(nums[i],nums[j]))
            if nums[j] != nums[i]:
                count = 1#reset
                i += 1
                nums[i] = nums[j]#first num
            elif nums[j] == nums[i]:
                if count == 1:
                    i += 1
                    nums[i] = nums[j]#second num
                    count += 1
                elif count > 1:#do nothing ,just j++
                    count += 1
                elif count == 0:#init
                    count += 1
        return i + 1

    # 隔2法，纯粹靠距离，前边2也得先避开不处理。
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     i=0
    #     for n in nums:
    #         if i<2 or n>nums[i-2]:
    #             nums[i]=n
    #             i+=1
    #     return i

    # 一个三指针的方法，i和j仍然管赋值，k是负责存住上一次的值，其实类似二跨度法。
    def removeDuplicates(self, nums):
        n = len(nums)
        if (n <= 2):
            return n
        # nums[0...i]是符合要求的，
        i = 1
        k = i - 1
        j = i + 1

        while j <= n - 1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                k = i
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1


list = [1,1,1,1,2,2,2,3]
print(list)
s = Solution()
length = s.removeDuplicates(list)
string = ''
for i in range(length):
    string += str(list[i])+', '
print(string)