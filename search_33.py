#  搜索旋转排序数组
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 你可以假设数组中不存在重复的元素。
# 你的算法时间复杂度必须是 O(log n) 级别。

# 思路，循环数组，mid的计算特殊处理。但是也不是绝对的O(logn），最起码找到起始点还需要n的吧？
class Solution:
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n == 0:
    #         return -1
    #     elif n == 1:
    #         if target == nums[0]:
    #             return 0
    #         return -1
    #     elif n == 2:
    #         if target == nums[0]:
    #             return 0
    #         elif target == nums[1]:
    #             return 1
    #         else:
    #             return -1
    #     right = n-1
    #     for i in range(len(nums)-1):
    #         if nums[i] > nums[i+1]:
    #             right = i
    #             break
    #     left = (right + 1) % n
    #     # print(left,right)
    #     # mid = (left + ((right + n - left)  // 2)) % n
    #     # print('mid:',mid)
    #     while left != right:
    #         print('left&right:',left,right)
    #         if right < left:
    #             mid = (left + ((right + n - left)  // 2)) % n
    #         else:
    #             mid = (left + right) // 2
    #         # print('mid:',mid)
    #         if target > nums[mid]:
    #             left = ( mid + 1 ) % n
    #         elif target < nums[mid]:
    #             if right == left + 1:
    #                 print('break')
    #                 break
    #             right = ( mid - 1 ) % n
    #         else:
    #             return mid
    #
    #     # if left == right:#no need
    #     if nums[left] == target:
    #         return left
    #     return -1

    # 不想用这个弱智模板，太麻烦

    # 简单的写法反而通过了
    def search_mysel(self, nums, target):
        if not nums:
            return -1
        n = len(nums)

        right = n-1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                right = i
                break
        left = (right + 1) % n

        def search_func(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        if left > right:
            if -1 == search_func(nums[left:]+nums[:right + 1],target):
                return -1
            return (search_func(nums[left:]+nums[:right + 1],target) + left) % n
        else:
            return search_func(nums,target)
        return -1



    # 真正的logN算法
    #最推荐的方法，逻辑简洁明了：如果左区间有序，并且target在左区间，就去左区间找，否则去右；如果右区间有序，并且target在右区间，就去右区间找，否则去左。
    def search_other(self, nums, target):#44ms
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            #首先确定mid属于哪个有序序列中
            elif nums[mid] >= nums[left]:    #确定在上个升序序列中，这里要注意针对数组中只有两个数时的边界问题，=号要放在这里，如果这里用等号，后面nums[mid] <= nums[right]就会陷入死循环,比如实例：[3,1]0
                #然后确定target属于哪个部分
                if target >= nums[left] and target < nums[mid]:   #双重条件才能确定target在mid的前半部分（升序序列的子序列），否则在后半部分（可能是两个升序序列的结合）
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid]<target and target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


    #logN算法，框架是二分查找，经过多个条件对比和处理
    #但是网课这个破逻辑明显不如上边那个简单清晰,可能是太过于强行套框架了？
    # 我不知道算不算生搬硬套二分查找框架，反正他的逻辑是，先区分target比mid大还是小，然后细分之后还可能推翻这个区分，细化一堆逻辑
    #强行抄下来以后，答案却是对，但是确实乱，你target小于mid，搞一堆begin和mid的判断，你target大于mid，还用begin和mid，这就太乱了
    #他的左右侧都用同一种逻辑，是因为判断哪边升序哪边旋转的逻辑根本不该放在最后，如果真的放最后，你最好用对应的逻辑，别用同一套逻辑
    def search(self, nums, target):
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            # 二分查找的主体框架是target比mid大或者小
            # 但是旋转数组的话这个逻辑又是错的，所以在细分的逻辑里还得兜回去
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[begin] < nums[mid]:#有序区间
                    if target >= nums[begin]:#true
                        end = mid - 1
                    else:##false：推翻了前边的逻辑，还得往另一个区间跑
                        begin = mid + 1
                elif nums[begin] > nums[mid]:#乱序区间:这块才是关键逻辑，前边已经确定了target比mid小，但是这块逻辑并不能说明问题，而是隐含的右侧区间有序，才证明target比右侧的都小
                    end = mid - 1
                elif nums[begin] == nums[mid]:#如果持平了，他就再进一格，再尝试
                    begin = mid + 1
            elif target > nums[mid]:
                if nums[begin] < nums[mid]:
                    begin = mid + 1
                elif nums[begin] > nums[mid]:
                    if target >= nums[begin]:
                        end = mid - 1
                    else:
                        begin = mid + 1
                elif nums[begin] == nums[mid]:
                    begin = mid + 1

        return - 1

            # elif target > nums[mid]:
            #     if nums[mid] < nums[end]:
            #         if target < nums[end]:
            #             begin = mid + 1
            #         else:
            #             end = mid - 1
            #     elif nums[mid] > nums[end]:#rotated    nums[begin] < nums[mid]
            #         begin = mid + 1
            #     elif nums[mid] == nums[end]:
            #         begin = mid - 1




nums = [4,5,6,7,0,1,2]
nums = [4,5,6,7,0,1,2]
target = 6
nums = [4,5,6,7,0,1,2]
target = 3
nums = [1,3]
target = 4
nums = [1,2,3,6,7,9]
target = 0
nums = [3,1]
target = 0
nums = [4,5,6,7,0,1,2]
target = 1
nums = []
target = 5

# print(nums[3:])

s = Solution()
print('ret:',s.search(nums,target))