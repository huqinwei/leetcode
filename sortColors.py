#Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
#warning:it is a sorted array....
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
        '''
        c0 = 0
        c1 = 0
        c2 = 0
        n = len(nums)
        for c in range(n):
            if nums[c] == 0:
                c0 += 1
            elif nums[c] == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(c0):
            nums[i] = 0
        for j in range(c1):
            nums[c0 + j] = 1
        for k in range(c2):
            nums[c0 + c1 + k] = 2





array = [1,1,1,2,2,0,0]
array2 = []
print(array)


s1 = Solution()
print(s1.sortColors(array))
# print(s1.removeDuplicates(array2))
print(array)


