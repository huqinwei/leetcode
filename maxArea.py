class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        r = len(height) - 1
        l = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


for i in range(4,10):#reverse
    print(10  + 4 - i)
# print(min(3,4))

s1 = Solution()
ret = s1.maxArea([1,8,6,2,5,4,8,3,7])
print('ret:',ret)


