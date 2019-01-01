# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。

import time
class Solution:
    def combinationSum2(self, candidates, target):#1444ms,可以过，但是很慢，也许后边的遍历转化太耗时
        candidates.sort()
        result = []
        temp_result = set()

        def func(s,sub_list, nums):
            if s > target:
                return
            if s == target:
                temp_result.add(tuple(sub_list))
                return
            if not nums:
                return
            func(s,sub_list, nums[1:])
            func(s+nums[0],sub_list + [nums[0]], nums[1:])
        start = time.time()
        func(0,[], candidates)
        end = time.time()
        print('phase 1, spend ',end - start)
        start = time.time()
        for v in temp_result:
            result.append(list(v))
        end = time.time()
        print('phase 2, spend ',end - start)#但是看数量级，并没有那么大
        return result


    def combinationSum2_other(self, candidates, target):#80ms
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.resList = []
        fl = [0] * len(candidates)
        candidates = sorted(candidates)
        self.dfs(candidates, [], target, fl, 0)
        return self.resList

    def dfs(self, candidates, sublist, target, flaglist, last):
        if target == 0:
            self.resList.append(sublist[:])
        if target < candidates[0]:
            return
        l = None  # 为了防止重复的比如两个1， 在一层递归只处理一次
        for m in range(len(candidates)):
            n = candidates[m]
            if n > target:
                return
            if n < last or flaglist[m] == 1 or l == n:
                # 三种情况：1.因为是从小到大，所以n开始要从上一个数以后
                # 2.如果已经使用过，那就继续
                # 3.如果在这一层递归的时候 比如有两个1，那之前做一次1的时候，第二次就不处理了，不然会重复
                continue
            sublist.append(n)
            flaglist[m] = 1
            self.dfs(candidates, sublist, target - n, flaglist, n)
            flaglist[m] = 0
            l = n
            sublist.pop()
nums = [2,1,2,3]
sol = Solution()
ret = sol.combinationSum2(nums,4)
print('ret:',ret)
