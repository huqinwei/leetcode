class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''
        count = 0
        length = len(nums)
        i = 0
        while i != length - count:
            print('i=',i,':',nums[i])
            if nums[i] == val:
                count += 1
                for j in range(i,length - 1):
                    nums[j] = nums[j+1]
                i -= 1
            i += 1
            # print(nums)

        return length - count
        '''
        n = len(nums)
        i = -1
        j = 0
        count = 0
        # nums[0....i]表示非0元素的数列,初始值i=-1
        while j <= n-1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            else:
                count += 1
            j += 1
        # for k in range(i+1, n):
        #     nums[k] = 0
        return n - count


array = [2,2,0,2,21,1,1,3,3,1,0]
print(array)


s1 = Solution()
print(s1.removeElement(array,2))
print(array)


