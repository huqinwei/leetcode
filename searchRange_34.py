class Solution:
    def searchRange_old(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1

        if left == right:
            if target == nums[left]:
                return [0, 0]

        while left <= right:
            mid = (left + right) // 2
            # print('left:',left,' right:',right,' mid:',mid)
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:  # ==target
                left = right = mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1

                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1

                return [left, right]
        return [-1, -1]
    def searchRange(self, nums, target):
        left = -1
        right = -1
        if nums == []:
            return [left,right]
        def searchLeft(nums, target):
            if not nums:
                return 0
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return right

        def searchRight(nums, target):  ##做一个完全逆向，包括起点区间，包括计算中点的偏向
            if not nums:
                return 0
            left = -1
            right = len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return right

        left = searchLeft(nums, target)
        right = searchRight(nums, target)

        if left > right:
            return [-1,-1]
        return [left,right]



A = [-1,2,5,20,20,20,20,800]

sol = Solution()
print('ret:',sol.searchRange_old(A,20))



def searchLeft(nums, target):
    if not nums:
        return 0
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return right
def searchRight(nums, target):##做一个完全逆向，包括起点区间，包括计算中点的偏向
    if not nums:
        return 0
    left = -1
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return right
A = [-1,2,5,20,20,20,20,800]
A = [-1,2,5,20,20,20,20]
A = [5,7,7,8,8,10]
print(searchLeft(A,8))
print('right:',searchRight(A,8))


#
#
#
#
# B = [50,90,3,-1,207,80]
#
# n = len(B)
# C = n * [0]
# finish_point = n * [0]
# print(C)
# for i in range(n):
#     search = B[i]
#     r = len(A)
#     l = 0
#     while l < r:
#         mid = (l+r) // 2
#         if search == A[mid]:
#             C[i] = 1
#             break
#         if search > A[mid]:#关于循环会卡住，要让循环终结。其实这个关键点也很好找，l对应4，r对应6，你要search5，就看这个卡住的点，因为左侧的点肯定比过了，所以就让左边更进一步
#             l = mid + 1
#         else:
#             r = mid
#     # 当然，本例没必要用这种方法，这种方法应该还能拿出最后一个元素进行一些处理
#     # 而且我这样找法，根据移动l和移动r不同，可以做不同的操作?????NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     #4,6之间找5，如果是移动l，最后找到的是6，移动r，最后找到的是4??不光是这样，看下边的例子!!!!!!!!!!!!
#     else:#只是打印出来作为对比
#         print('l is ',l)
#         finish_point[i] = A[l]#找到的都走不到这个循环，所以对应元素是0
#
# print(C)
# print('finish_point 1:',finish_point)









# 网课的左断点

A = [-1,2,5,20,20,20,20,800]
def left_bound(nums,target):

    begin = 0
    end = len(nums) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if target == nums[mid]:
            # if mid == len(nums) - 1 or nums[mid+1] > target:#ppt错了
            if mid == 0 or nums[mid-1] < target:
                return mid
            # begin = mid + 1
            end = mid - 1
        elif target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            begin = mid + 1
    return -1


print('ret:',left_bound(A,20))









