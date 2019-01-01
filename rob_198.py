
#
# 198. 打家劫舍
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。




# 这个问题，当你选中一个房屋i-1后，那么i得空出来，剩下你从i+1和i+2选中一个最优，这肯定是不够的。
# 例如，5,10,100,5,10，如果因为10比5大，那么100就浪费了，所以你的视野至少达到3.
# i空出来以后，要考虑i+1,i+2,i+3，如果i+3很大，肯定舍弃i+2了。那假如最后一个是i+4，你还得从i+1+i+3和i+2+i+4之间选择一个。
# 所以视野是4才够？如果是这样，还要不要考虑i+5的情况？所以找出这个分界点才是关键

#这个看起来有贪心的思想，却无从下手，其实贪心不一定要从前往后找

# 如果从大往小找，不还是面临那种情况，万一某一个局部就反转了呢？
# 比如100,90,50,80，贪心找100,90就错过，那么就剩90+80，其实大于100+50，但是这里倒是还能跳，100之后直接80，总共180.这个例子看起来也满足。
# 假如是100,90,50,80,70呢？那100+80其实小于100+50+70.我居然跳不出来这个困境。。。。。
# 看起来好像有这么一条规则，你选择某一条i的时候，可能错过i-1和i+1，所以其实你是在比i和[i-1]+[i+1]


#纸上画起来，貌似有点规律，但是需要改的有点远，当前是i的话，往前能改好几步
# 5,2,6,3,1,7,9,11,13
# 遇到13之前，是5,6,7,11，而遇到13之后，是5,6,1,9,13
#好像需要一直往前找，找到能改变的那一点，然后对比改变前后的值，确定是否改变。像5和6都是稳定的，都不能改，
# 为什么是稳的，为什么不能让6也换成3？因为2+3小于6？所以6的位置是稳的？
# 而这种一直变化的，1,7,9,11，不服从这种规律。而3之后无论是1还是100,6都不用屈服，因为他俩已经隔开了。大概是这个规律吧，一个数，如果左右的和小于他，他就是稳的。
# 我还能找到什么反例能推翻它吗？看起来是推不翻了，大概是这个规律
# 大概是这个规律，但是在一个长序列中，怎么确定某一个数是稳的，还是需要改的时候再判断？
#或者我逐渐把队列或者是盗窃队列加起来的时候，往前找到稳定的数字时停止。
# 其实逐渐拉长队列，无非两种状态，i和i+2更大，i+1和i+3更大，如果i比左右都大，那无非是i和i+2或者i和i+3组合。

#实际上我想的和他的动态规划算法差不多了。只不过我说的i比左右的和都大，其实转换成i比右大就行了，i比左大的情况是在过去的遍历中决定的，仔细想想也是，我一直往右看，没往左看，我以为i比[i-1]大就可以，其实考虑连锁反应，不一定可以：2,6,3,6比2+3大，换个例子，1000，100,4,6,1，虽然6比4+1大，但是明显1000+4+1更优，所以这个东西不能回头看，一定是向前看。

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
# 那么既然不能回头，而是在过去就要选好，那么他是怎么确定前边i-1个的？
# 如果选择第i个房间，就不能选第i-1个房间。
# 如果不选择第i个房间，相当于只考虑前i-1个房间。
#
# 答案要的是总数，不用具体的下标，他规划的也是数值，其实仔细看，他的逻辑不是用的下标，是用的max操作：
#
# [5,2,6,3,1,7]
#
# dp[1] = 5
# dp[2] = 5
# dp[3] = max(dp[1]+nums[3],dp[2])
# dp[4] = max(dp[2] + nums[4],dp[3])
#
# dp[i] = max(dp[i-2] + nums[i],dp[i-1])
#
# 其实他靠这个传递了更早的值，比较不选i-1的情况下加上nums[i]和选了[i-1]不加nums[i]的情况。
# 所以你看，真正的细致的传导下标来操作会很麻烦，他也是利用嵌套，间接的把很早的数值直接传到当前来考虑。
# 其实不管nums[i-2]你有没有加进来，他都叫做dp[i-2]。在你确定不选i-1的时候dp[i-2]没问题。
# 所以，精髓就是，dp传递的值不在乎你具体选没选某一个值，而是一个状态，就是只考虑前多少个元素的时候，他就是最大的。

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
# def climbStairs(self, n):
#     dp = (n + 3) * [0]  # 他这个写法，反而能达到简洁的效果
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]


nums = [1,2,3,1]# 输出: 4

# nums = [2,7,9,3,1]# 输出: 12

class Solution:
    def rob_myself(self, nums):
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n <= 2:
            return max(nums[0],nums[1])

        dp = (n) * [0]
        dp[0] =nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        # print(dp)
        return dp[n-1]


    def rob(self, nums):#尝试简化代码
        n = len(nums)#
        dp = (n+1) * [0]
        # 打家劫舍和爬楼梯不一样，就是要从nums中拿数据，预先做一个更长的dp应该也不能简化代码？我能怎么阻止数组越界？
        dp[0] = 0
        if n >= 1:#除了nums，访问由我自己控制，所以总长n+1，如果n够大，再去从nums拿就行了
            dp[1] = nums[0]

        # dp[1] = max(nums[0],nums[1])
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        # print(dp)
        return dp[n]


sol = Solution()
print('ret:',sol.rob(nums))




