class Solution:
    def moveZeroes_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        length = len(nums)
        i = 0
        while i != length - count:
            print('i=',i,':',nums[i])
            if nums[i] == 0:
                count += 1
                for j in range(i,length - 1):
                    nums[j] = nums[j+1]
                i -= 1
            i += 1
            print(nums)

        for i in range(count):
            # print('i:',i)
            nums[length-i-1] = 0
        # print(nums)

    def moveZeroes_v2(self, nums):
        n = len(nums)
        i = -1
        j = 0
        # nums[0....i]表示非0元素的数列,初始值i=-1
        while j <= n-1:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1, n):
            nums[k] = 0

    def moveZeroes(self,nums):
        n = len(nums)
        i = -1
        j = 0
        while j < n:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i+1,n):
            nums[k] = 0
        print(nums)


#different from c
# for i in range(10):
#     print(i)
#     if i == 5:
#         i -= 1


array = [2,2,0,2,21,1,1,3,3,1,0]
print(array)


s1 = Solution()
s1.moveZeroes(array)
print(array)


