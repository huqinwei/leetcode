# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

'''
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
'''
# 目标肯定是尽可能用更多更大的数字来跳，可能的实现思路是查找当前i对应能跳到的位置，哪个大要哪个？
# 其实还要补充，要加上i来比，当前i对应的nums[i]，他覆盖的[i:nums[i]+i+1]范围，要看谁的nums[i]+i更大，比如[4,3,2,1,1]，明显不是选3,而是选最后一个1
class Solution:
    def jump(self, nums):#AC:132ms
        count = 0
        jump_to = 0
        for i in range(len(nums)):
            if i == jump_to:
                if i == len(nums) - 1:#最后一个位置，肯定要跳到那，但是如果刚开始就是最后一个位置，就不跳了，算0
                    return count
                else:
                    max_next_jump = 0
                    count += 1
                    for j,val in enumerate(nums[i:nums[i]+i+1]):
                        if i + j >= len(nums) - 1:# 光是判断谁大是不对的，[2,3,1]中3能跑的更远，但是1已经到终点了,优先判断一步到位，其次更新最大跳跃
                            jump_to = len(nums) - 1
                            break

                        if i+j+nums[i+j] > max_next_jump:
                            max_next_jump = i+j+nums[i+j]
                            jump_to = i+j

                    # if max_next_jump >= len(nums):##没有这些多余的逻辑，就两种情况，如果这一步就能到终点，前边已经break了，如果这一步到不了，就别break谁了，肯定得让这一步走完，乱break反而打乱了逻辑
                    #     jump_to = len(nums) - 1
                    #     print('break')
                    #     break#这是一层小循环，contnue跳不出去

        return count
    #主ti思路肯定不会有差距，主要是边角的处理，这个更简洁
    # 尤其是一步不走的情况，因为pos==current_max==0，不触发cnt+=1,因为pos自带+=1，所以再然后，就没有然后了
    def jump(self, nums):
        cnt, n_nums = 0, len(nums)
        history_max = current_max = pos = 0
        while pos < n_nums:
          # 记录历史中可以到达的最远距离
          if pos > current_max:
            # pos已经超过最远可到的位置，必需跳
            current_max = history_max
            cnt += 1
          history_max = max(history_max, pos + nums[pos])
          pos += 1

        return cnt
nums = [2,3,1,1,4]

# nums = [2,1]
# nums = [0]
# nums = [1,2,3]
# nums = [2,3,1]
sol = Solution()
print('ret:',sol.jump(nums))



