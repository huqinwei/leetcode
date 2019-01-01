class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dicti = set(), {}
        numLen = len(nums)
        nums.sort()
        for i in range(numLen):
            for j in range(i+1, numLen):
                key = nums[i] + nums[j]
                if key not in dicti.keys():
                    dicti[key] = [(i,j)]
                else:
                    dicti[key].append((i,j))
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                exp = target - nums[i] -nums[j]
                if exp in dicti.keys():
                    for tmpIndex in dicti[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        return [list(i) for i in res]
# 遍历，把两个数的和当key，存起来，变成3sum。然后，3sum他也没用更繁琐的算法，就用了O(n^2)的遍历，结果用set存储就能去重！
# 别看不起O(n^2)，当你的问题逐渐往n^3乃至更高攀升的时候，多加一个O(n^2)好像并没有什么影响。