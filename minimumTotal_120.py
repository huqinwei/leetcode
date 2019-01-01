# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#

#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#
#
#
#
# 这个题是从顶端到底端画出一条路径，让这个路径和最短。
#
# 动态规划好像都这样，肯定不是让你可以直白想明白的，所以必须拉出来状态的变化过程。
# 三角形，贪婪，肯定也不行，从上边看，如果贴着左边走最小，到底下却发现右边最小，但是你过不去了，得回溯。
#
# 具体的，所谓相邻，应该是下一行的i和i+1选一个
# dp应该是走到每一层的时候路径和最小？
# dp[0]是2
# dp[1]是2+3
# dp[2]是2+3+5
# dp[3]是2+3+5+1
# 这个例子太简单，没有需要回溯的情况。关键在于设计回溯。
# 但是如果我dp存的只是当前最优路径，dp[i]从dp[i-1]得到的不是最优怎么办？如果存的信息只有这些，又怎么知道到dp[i]是不是最优？
# 想找倒是也不难，你不是拿到i-1了吗？遍历i-1这一行都能办到。
#
#
# 动态规划既然叫做动态规划，而不叫贪心，肯定不能简单就保存一个当前最优（但是你要的答案却是就是当前最优），就算是，也是能从前边推出后边的，我觉得这叫数学归纳法。
#
# ##################################################################
# 所以，空想了半天，之前的思路并不能解决问题，dp升级了，成二维的了！！！！！！

#dp[i][j]代表第i行、第j列的最优解，而不是单纯就是到第i行，这样看起来就可行一些了。指定一个终点，找到路径。这样最后把dp[i]对应的所有j都遍历一下，对比就行了吧？
# 然后d[i][j]可以由d[i-1][j]和d[i-1][j-1]推出，然后我d[i][j]就从二者之中选最小，加上nums[i][j]，就是d[i][j]
#
# d[i][j] = min(d[i-1][j],d[i-1][j-1] if exist)
# 这个if条件要有的，因为j=0的时候没有对应的-1下标
class Solution:
    def minimumTotal_myself_v1(self, triangle):#这是我看一眼他的dp[i][j]，没看更多，就有了灵感，自己做出来了，果然DP还是要多做，就是个熟练活。

        dp = []

        #way 1 to create dp
        # for i in range(len(triangle)):
        #     dp.append([])
        #     for j in range(len(triangle[i])):
        #         dp[i].append(0)
        #way 2
        for i in range(len(triangle)):
            dp.append([])
            dp[i].extend(len(triangle[i]) * [0])#extend不是append

        #way 3
        # print(dp)

        #初始化和赋值先分开，不过我觉得可能这两部能合并
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                #这个地方要特别注意，[i-1][j]不一定存在的，[i-1][j-1]也不一定存在。三角形啊，i比i-1多了一个，考虑左右边界，那不就是两边都可能少嘛
                if j - 1 >= 0 and j < len(triangle[i-1]):
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
                elif j - 1 >= 0:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                elif j < len(triangle[i-1]):
                    dp[i][j] = dp[i-1][j] + triangle[i][j]

        min_track = 0
        for k in range(len(dp[-1])):
            # print(dp[-1][k])
            if k == 0:#init
                min_track = dp[-1][k]
            min_track = min(min_track,dp[-1][k])
        return min_track


    def minimumTotal_myself_v2(self, triangle):#稍微优化一下创建数组的过程,合并进大循环
        dp = []
        for i in range(0,len(triangle)):
            dp.append([])

            for j in range(len(triangle[i])):
                new_value = 0#dp[i][j]
                if i == 0:#0特殊，还是得处理，放哪都要特殊处理,不管放前边放后边，总之逃不掉
                    new_value = triangle[i][j]
                else:
                    if j - 1 >= 0 and j < len(triangle[i-1]):
                        new_value = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
                    elif j - 1 >= 0:
                        new_value = dp[i-1][j-1] + triangle[i][j]
                    elif j < len(triangle[i-1]):
                        new_value = dp[i-1][j] + triangle[i][j]
                dp[i].append(new_value)#dp[i][j] == new_value,其实这样替换完反而不直观

        min_track = 0
        for k in range(len(dp[-1])):
            if k == 0:#init
                min_track = dp[-1][k]
            min_track = min(min_track,dp[-1][k])
        return min_track

    def minimumTotal_myself_v3(self, triangle):#再做一优化，把最后的遍历合并进大循环
        dp = []
        min_track = 0
        for i in range(0,len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                new_value = 0#dp[i][j],其实这样替换完反而不直观
                if i == 0:#0特殊，还是得处理，放哪都要特殊处理,不管放前边放后边，总之逃不掉
                    new_value = triangle[i][j]
                else:
                    if j - 1 >= 0 and j < len(triangle[i-1]):
                        new_value = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
                    elif j - 1 >= 0:
                        new_value = dp[i-1][j-1] + triangle[i][j]
                    elif j < len(triangle[i-1]):
                        new_value = dp[i-1][j] + triangle[i][j]
                dp[i].append(new_value)
                if i == len(triangle)-1:#最后一层开始找最短路径
                    if j == 0:#init
                        min_track = new_value
                    min_track = min(min_track,new_value)
        return min_track
#########################################################################
# 重点是，他讲的例子是从下到上的去思考，和我的模式不一样，！！！！

#########################################################################
    # 反正都是找路径，从下往上从上往下没有本质的区别，顶多就是下标不一样，而且从下往上找的话，最后结果不用筛选
    # 这种的边界确实好处理，简洁，不过前边那种化简不行，dp必须一次性声明完，才能从后往前填充
    def minimumTotal(self, triangle):
        dp = []

        for i in range(len(triangle)):
            dp.append([])
            dp[i].extend(len(triangle[i]) * [0])#extend不是append

        for i in range(len(dp)-1,-1,-1):#dp,triangle,len都一样
            for j in range(len(dp[i])):
                dp[i][j] = triangle[i][j]#common part
                if i == len(dp) - 1:
                    pass
                else:#update dp[i][j]###下一层的j和j+1，这个比从上到下好像判断条件简单多了
                    dp[i][j] += min(dp[i+1][j],dp[i+1][j+1])

        return dp[0][0]



## 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

sol = Solution()
print('ret:',sol.minimumTotal(triangle))











