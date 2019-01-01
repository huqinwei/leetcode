import collections
'''
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
注意:

数组的长度不会超过20，并且数组中的值全为正数。
初始的数组的和不会超过1000。
保证返回的最终结果为32位整数。
'''


class Solution:
    def findTargetSumWays_slow(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        n = len(nums)
        if nums == []:
            return 0

        new_array = []
        cur_index = 0
        for i in ['+','-']:
            if i == '+':
                new_array2 = new_array.copy()
                new_array2.append(nums[cur_index])
                # print('new_array2:',new_array2)
                self.dfs_slow(cur_index+1,nums,new_array2,S)
            if i == '-':
                new_array2 = new_array.copy()
                new_array2.append(-nums[cur_index])
                # print('new_array2:',new_array2)
                self.dfs_slow(cur_index+1,nums,new_array2,S)

        return self.cnt

    def dfs_slow(self,cur_index,nums,new_array,S):
        if cur_index < len(nums):
            for i in ['+','-']:
                if i == '+':
                    new_array2 = new_array.copy()
                    new_array2.append(nums[cur_index])
                    self.dfs_slow(cur_index+1,nums,new_array2,S)
                if i == '-':
                    new_array2 = new_array.copy()
                    new_array2.append(-nums[cur_index])
                    self.dfs_slow(cur_index+1,nums,new_array2,S)
        else:
            # print('new_array:',new_array)
            if sum(new_array) == S:
                self.cnt += 1
    # 时间超了，但是想不到什么去重的方法啊，没有visited，根据例子，4个1和1个-1，能有5种情况，每一个都是独立的。
    # 那么唯一问题可能就是递归调用效率低？
    # 如果用栈，怎么复制list呢？或者我应该只存符号？前边的例子是复制占了时间？可能是操作不熟，不应该纠结，直接看答案


    # 实测：不复制是万万不能的
    def findTargetSumWays_v2(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt = 0
        n = len(nums)
        if nums == []:
            return 0

        symbol_array = []
        cur_index = 0

        symbol_array2 = symbol_array.copy()
        self.dfs_v2(cur_index,nums,symbol_array2,S)

        return self.cnt

    def dfs_v2(self,cur_index,nums,symbol_array,S):
        # print('cur:',cur_index)
        if cur_index < len(nums):
            for i in ['+','-']:
                if i == '+':
                    symbol_array2 = symbol_array.copy()
                    symbol_array2.append(i)
                    self.dfs_v2(cur_index+1,nums,symbol_array2,S)
                if i == '-':
                    symbol_array2 = symbol_array.copy()
                    symbol_array2.append(i)
                    self.dfs_v2(cur_index+1,nums,symbol_array2,S)

        else:
            # print('new_array:',new_array)
            sum = 0
            # print('symbol:',symbol_array)
            # print('nums:',nums)
            for i,v in enumerate(symbol_array):
                # print(i,v)
                if v == "+":
                    sum += nums[i]
                elif v == "-":
                    sum -= nums[i]

            # print('sum:',sum)
            if sum == S:
                self.cnt += 1

    # 如果用栈存符号，碰到不一样的就出栈一个，比如[+++]，遇到[-]就是[++]，再遇到[+]，最终[+++]，不过这种就没法区分到底是第几下标正了，
    # 只靠分支来天然的区分。但是复杂度什么的没变吧，最后还不是要看剩下的几个加号？和5个符号都保留能差多少？
    # 只看剩余几个符号不能解题，因为nums不一定都是1

    #leetcode专题很骗人，他告诉你这个可以用BFS，实际上DFS更快，他把这个扔进DFS，其实DFS又超时
    # 这是别人的DFS，也超时了，不过很简洁。
    # return 1是正确，0是错误，最后return的就是count。
    # 没有多余存储结构，直接用acc存好计算中的sum，每一步直接递归index和acc
    # def findTargetSumWays(self, nums, S):
    #     """
    #     :type nums: List[int]
    #     :type S: int
    #     :rtype: int
    #     """
    #     def helper(index, acc):
    #         if index == len(nums):
    #             if acc == S:
    #                 return 1
    #             else:
    #                 return 0
    #         return helper(index + 1, acc + nums[index]) + helper(index + 1, acc - nums[index])
    #     return helper(0, 0)



    # "动态规划我做的不多，这个题也算是开了个小头。设了一个数组，数组中保存的是字典，字典保存的是该index下的能求得的和为某个数的个数。"
    # "所以从左到右进行遍历，在每个位置都把前一个位置的字典拿出来，看前一个位置的所有能求得的和。和当前的数值分别进行加减操作，就能得出新一个位置能求得的和了。"



    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        _len = n
        dp = [collections.defaultdict(int) for _ in range(n + 1)]#dp比nums长度多一个
        dp[0][0] = 1#第0次迭代，求和为0，出现了1次，这是一个初始化，后边才开始加数字
        # 后边就开始迭代真正的sum和出现的次数，1和 - 1都出现了一次。
        # 再迭代：2出现1次，0出现一次，-2出现一次，0出现一次，这时候0就是两次了， += cnt就是这么来的

        for i,num in enumerate(nums):#nums每个元素都是一次迭代
            #把前一次的结果从defaultdict取出来，迭代到后一次
            for sum,cnt in dp[i].items():# items并不是dict所有元素的sum and元素个数cnt，sum和cnt是他自定义的逻辑，其实这个就是遍历字典
            # for sum, cnt in dp[i]:  # TypeError: 'int' object is not iterable
                dp[i+1][sum+num] += cnt
                dp[i+1][sum-num] += cnt

        return dp[n][S]#过渡性的，前边的都没用了，直取最后一个


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1],3))

# "要注意一点是，dp初始不能采用下面方式：
# dp = [collections.defaultdict(int)] * (_len + 1)
# 这种初始化方式会使每个位置的元素其实是同一个字典。
dp = [collections.defaultdict(int)] * (4 + 1)
print(dp)
dp = [collections.defaultdict(int) for _ in range(4 + 1)]
print(dp)

dpi = collections.defaultdict(int)
print(type(dpi))
dpi[0] = 1
dpi[-1] = 1
for i,j in dpi.items():
    print('i,j:',i,j)
# for i,j in dpi:#TypeError: 'int' object is not iterable
#     print('i,j:',i,j)

