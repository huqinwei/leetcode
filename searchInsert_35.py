# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
            print('left is ',left,' right is ',right)
        return left


A = [-1,2,5,20,90,100,207,800]

sol = Solution()
print('ret:',sol.searchInsert(A,801))




A = [-1,2,5,20,90,100,207,800]

B = [50,90,3,-1,207,80]

n = len(B)
C = n * [0]
finish_point = n * [0]
print(C)
for i in range(n):
    search = B[i]
    r = len(A)
    l = 0
    while l < r:
        mid = (l+r) // 2
        if search == A[mid]:
            C[i] = 1
            break
        if search > A[mid]:#关于循环会卡住，要让循环终结。其实这个关键点也很好找，l对应4，r对应6，你要search5，就看这个卡住的点，因为左侧的点肯定比过了，所以就让左边更进一步
            l = mid + 1
        else:
            r = mid
    # 当然，本例没必要用这种方法，这种方法应该还能拿出最后一个元素进行一些处理
    # 而且我这样找法，根据移动l和移动r不同，可以做不同的操作?????NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #4,6之间找5，如果是移动l，最后找到的是6，移动r，最后找到的是4??不光是这样，看下边的例子!!!!!!!!!!!!
    else:#只是打印出来作为对比
        print('l is ',l)
        finish_point[i] = A[l]#找到的都走不到这个循环，所以对应元素是0

print(C)
print('finish_point 1:',finish_point)