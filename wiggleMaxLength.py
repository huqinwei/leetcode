
# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
#
# 例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#
# 给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。
#

# 感觉就是简单遍历，这里注意一点就行吧，就是每次失败了，重置长度不是0

class Solution:
    def wiggleMaxLength_wrong(self, nums):#少看了一句话，他可以在里边删除元素，自由组合，这也叫子序列。。。。
        max_count = 0
        count = 0
        is_increment = None
        last_val = None
        for val in nums:
            if last_val == None:#init
                count += 1
                last_val = val
                continue

            sub = val - last_val
            print('sub:',sub)
            if is_increment == None:#init
                if sub > 0:
                    is_increment = True
                    count += 1
                elif sub < 0:
                    is_increment = False
                    count += 1
                else:#reset
                    #is_increment = None
                    count = 1
                    continue
            else:
                if is_increment == True:
                    if sub < 0:
                        count += 1
                        is_increment = False
                    else:#reset
                        count = 1
                        if sub > 0:
                            is_increment = True
                        else:#==0
                            is_increment = None
                        continue
                else:
                    if sub > 0:
                        count += 1
                        is_increment = True
                    else:#reset
                        count = 1
                        if sub < 0:
                            is_increment = False
                        else:#==0
                            is_increment = None
                        continue

            max_count = count

            last_val = val#update last_val


        return max_count
    def wiggleMaxLength_myself(self, nums):#AC
        last_val = None
        is_increment = None
        count = 0
        for val in nums:
            # print('last_val:',last_val)
            # print('count:',count)
            if last_val != None:
                sub = val - last_val
                if is_increment == None:
                    if sub > 0:
                        is_increment = True
                    elif sub < 0:
                        is_increment = False
                    else:
                        continue
                else:
                    if is_increment == True:
                        if sub < 0:
                            # count += 1
                            # last_val = val
                            is_increment = False
                        elif sub > 0:
                            # last_val = val
                            count -= 1#为了抵消统一的count++
                        else:
                            continue
                    else:
                        if sub > 0:
                            # count += 1
                            # last_val = val
                            is_increment = True
                        elif sub < 0:
                            count -= 1#为了抵消统一的count++
                        else:
                            continue

            count += 1
            last_val = val
        return count
class Solution:##和我时间一样的典型范例，算是用了一个宏
  UP, DOWN, BEGIN = 0, 1, 2

  def wiggleMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
      return len(nums)
    state = Solution.BEGIN
    cnt = 1
    for i in range(1, len(nums)):
      delta = nums[i] - nums[i - 1]
      if state == Solution.BEGIN:
        if delta == 0:
          state = Solution.BEGIN
        elif delta > 0:
          state = Solution.UP
          cnt += 1
        else:
          state = Solution.DOWN
          cnt += 1
      elif state == Solution.UP:
        if delta >= 0:
          state = Solution.UP
        else:
          state = Solution.DOWN
          cnt += 1
      elif state == Solution.DOWN:
        if delta <= 0:
          state = Solution.DOWN
        else:
          state = Solution.UP
          cnt += 1
    return cnt
input = [1,7,4,9,2,5]
# 输出: 6

input = [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
#
input = [1,2,3,4,5,6,7,8,9]
# 输出: 2
# 感觉遇到不合适的不更新last_val也不对，比如这样1,2,3,4,5,4，应该能到3的，但是不更新的话，应该还是2
input = [1,2,4,3]
#那应该是，如果当前状态同为增，且这个数字更大，更新；如果当前状态为减，切数字更小，更新。！
#但是这时候还不加count

sol = Solution()
print(sol.wiggleMaxLength(input))





