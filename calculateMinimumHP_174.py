# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由
# M
# x
# N
# 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
#
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至
# 0
# 或以下，他会立即死亡。
#
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为
# 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
#
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
#
#
#
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
#
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径
# 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为
# 7。
# 说明:
#
# 骑士的健康点数没有上限。
#
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

#乍一看像64，
# 如果我的动态规划是最终结果尽量大，然后顺便标记一下过程中最小出现负几？然后当做答案呢？
# 这是第一想法，但是题目没有这个要求，不是说总共费血最少的前提下，也就是说，面对最终总和-5，但是途中有-100的状态，总和-10，但是途中只有-10的状态，更优
# 所以每一步的筛选条件也变了，我追求的，就不是让当前的总和最大，而是当前血量最高。貌似也不能是从前两格推出当前？可能还是得用前两格推出当前，只是概念不同了
# 其实我dp就不该存总步数了，存当前血量
# 然后选择让当前血量最大的，然后我可以更新一个路径中最小血量？但是dp是把整个表格都推导出来，不是选定了一个路径。但是貌似我用dp规则好像能找回来？
# 有没有可能因为贪心掉进陷阱？如果我只求当前血量大，然后按着路径走到一个胡同，都是大的扣血
# 比如你一直向右，然后向下，最后到了一个大坑
# grid = [
#   [1,1,1],
#   [-1,-1,-100],
#   [-4,-2,1],
# ]
#所以这题是困难！这个动态规划确实不好想，主要有些条件不是单向的
# 之前的动态规划，关注的就是一个特性，总步数最小。
# 好像想问题方式错了，难道之前的问题没有这个坑？难道不能是一路小跑，突然来个大奖励？最终的结果把所有情况都考虑好了，结果会选出最合适的，其实没必要担心前边，生成dp是从前向后，其实dp的意义是后边的筛选前边的。
# 所以这个算法应该是，就以当前血量为dp？但是最后我要从结尾回溯到开始，找到一个最低点？
#实测，逻辑错误，不应该简单的判断大和小，得看是不是负的
# 宏观和微观不可兼得，逻辑想不通。可能更新dp的方式不够高级，这种推进方式是错的，有的dp能往前跳很多去找。
# 感觉逻辑还是要细化，不是简单看是否是负的，而是看和其他的互动之后，能达到什么水平dp[i][j]从前边筛选一个能让他尽量正的，但是如果都是正，有什么区别，不是max越大越好吗？我的逻辑就是这么走的
# dp应该是，之前走的所有步数中，数值最小的那个值？那也不对，我得决定当前。那就是，当前的值有多小？如果和历史最低比，不影响，就无所谓，但是无所谓的情况下，我怎么更新呢？更大更好？还是绕不开这个坑，肯定是dp的迭代方式有问题
# 推得顺序反了，我这一个点，如果要从左边和上边的历史中找，我自身对应的格子是固定的，其实我已经改变不了历史了。
# 正向推是二推一，反向推是一推二，也没有做出任何决定？
# 不是，反向也得二推一。但是我感觉一选二才是正确的走法？可能还是没在点上.动态规划还是hard，不自己抠了


class Solution:

    def calculateMinimumHP_failed(self, dungeon):
        if not dungeon:
            return 1
        if dungeon == [[0]]:
            # print('ret')
            return 1

        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                # print(dp[i][j])
                dp[i][j] = dungeon[i][j]
                if dp[i][j] < 0:#负的才要求越大越好，正的不一定，但是正的应该是什么逻辑？
                    if i > 0 and j > 0:
                        dp[i][j] += max(dp[i - 1][j], dp[i][j - 1])
                    elif i > 0:
                        dp[i][j] += dp[i - 1][j]
                    elif j > 0:
                        dp[i][j] += dp[i][j - 1]
                # else:




        i = len(dp) - 1
        j = len(dp[0]) - 1
        minimum = dp[i][j]
        while i>=0 and j>=0:
            print('i:',i,' j:',j)
            minimum = min(minimum,dp[i][j])
            if i - 1 >= 0 and j - 1 >= 0:
                if dp[i-1][j] > dp[i][j-1]:#等于的情况应该怎么选
                    i -= 1
                else:
                    j -= 1
            elif i - 1 >= 0:
                i -= 1
            else:
                j -= 1
        # print('minimum:',minimum)
        if minimum > 0:
            return 1


        return 1-minimum



#关键比较麻烦的是累积效应，可能代码功底弱了点，其实他这个方法也要间接累积的，3,2，-5，单看-5，需要-6,2呢，需要-4,3呢，需要1，
# 其实不是说这个格子本身需要1，他是正的，不需要，但是dp代表的是，需要的初始值是多少才能满足这个，因为是挖坑填坑，所以必须从后往前,因为前边可能有一定的积蓄，也就是免费帮你填坑
# 这题其实就是从后往前挖坑填坑碰到负的就挖坑，碰到正的就填坑，到最后，填不上的，就是初始值。
#这是一维的情况
# 二维的话，就是两个可能来的方向，选一个更大的值（更小的坑），然后就等于选择了路径？

    # 这个填坑方法一维很简单?错了!!!!!!二维的实现要考虑
    def calculateMinimumHP_failed2(self, dungeon):
        if not dungeon:
            return 1
        if dungeon == [[0]]:
            # print('ret')
            return 1

        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[0])-1,-1,-1):
                # print(dp[i][j])
                dp[i][j] = dungeon[i][j]

                if i + 1 < len(dp) and j + 1 < len(dp[0]) :
                    dp[i][j] += max(dp[i + 1][j], dp[i][j + 1])
                elif i + 1 < len(dp):
                    dp[i][j] += dp[i + 1][j]
                elif j + 1 < len(dp[0]) :
                    dp[i][j] += dp[i][j + 1]
        print(dp)
        if dp[0][0] <= 0:
            return 1
        return dp[0][0]


    #max操作才是关键，你后边的积蓄也不能用来填前边的坑,要时刻清零（他是按1算，至少1）
    # 这样个“清一”法，是为了最后最后不用再加1了，但是很不直观，确实绕
    def calculateMinimumHP_reset1(self, dungeon):
        if not dungeon:
            return 1
        if dungeon == [[0]]:
            # print('ret')
            return 1

        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        dp[-1][-1] = max(1,1-dungeon[-1][-1])
        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[0])-1,-1,-1):
                if i + 1 < len(dp) and j + 1 < len(dp[0]) :
                    dp[i][j] = max(1, min(dp[i + 1][j],dp[i][j+1]) - dungeon[i][j])#这里应该是min，因为dp表达的是需要满足的值，所以我应该找最少的
                elif i + 1 < len(dp):
                    dp[i][j] = max(1,dp[i + 1][j] - dungeon[i][j])#@dungeon要用上
                elif j + 1 < len(dp[0]) :
                    dp[i][j] = max(1,dp[i][j+1] - dungeon[i][j])#@dungeon要用上
        return dp[0][0]


    # 采用更直观的清零方式写出这个逻辑
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 1
        if dungeon == [[0]]:
            return 1

        dp = [[0 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
        #dp[-1][-1] = max(0,0-dungeon[-1][-1])
        for i in range(len(dp)-1,-1,-1):#这样写循环的话覆盖是全面，但是第一个元素要处理，扔到else或者放在上面
            for j in range(len(dp[0])-1,-1,-1):
                if i + 1 < len(dp) and j + 1 < len(dp[0]) :
                    dp[i][j] = max(0, min(dp[i + 1][j],dp[i][j+1]) - dungeon[i][j])#这里应该是min，因为dp表达的是需要满足的值，所以我应该找最少的
                elif i + 1 < len(dp):
                    dp[i][j] = max(0,dp[i + 1][j] - dungeon[i][j])#@dungeon要用上
                elif j + 1 < len(dp[0]) :
                    dp[i][j] = max(0,dp[i][j+1] - dungeon[i][j])#@dungeon要用上
                else:
                    # print('init')
                    # print(i,j)
                    dp[i][j] = max(0, 0 - dungeon[i][j])
        return dp[0][0] + 1

    #如果不看答案，哪怕换了方向推，哪怕想到dp是存那个需要的值,还是差点东西，这个题的核心是反向推的填坑挖坑方法，并且还要记得清零


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1],
]
grid = [
  [-2,-3,3],
  [-5,-10,1],
  [10,30,-5],
]
# grid = [[3,2,-5]]
# grid = [[-10,3,2,-5]]
# grid = [[-10,3,2,10,-5]]
# grid = [[0]]

print('ret:',Solution().calculateMinimumHP(grid))













