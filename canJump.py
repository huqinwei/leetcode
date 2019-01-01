# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#

# 示例 2:
#



class Solution:
    def canJump_myself(self, nums):#AC 84ms
        can_jump = []
        for i in range(len(nums)):
            can_jump.append(i + nums[i])
            # print('can_jump:',can_jump)
        current_max = 0
        for i in range(len(can_jump)):
            current_max = max(current_max,can_jump[i])
            print('current_max:',current_max)
            print('i:',i)
            if current_max <= i and i < len(can_jump) - 1:#特例，其实就是结尾的处理
                return False
        return True
    def canJump(self, nums):##其实不用单独生成数组，省一次循环#AC 80ms
        current_max = 0
        for i in range(len(nums)):
            current_max = max(current_max,i + nums[i])
            if current_max <= i and i < len(nums) - 1:#特例，其实就是结尾的处理
                return False
        return True

nums = [2,3,1,1,4]
# 输出: true
nums = [3,2,1,0,4]
# 输出: false
# nums = [0]#特例，其实就是结尾的处理
#true.....


sol = Solution()
print('ret:',sol.canJump(nums))



