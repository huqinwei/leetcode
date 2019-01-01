# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1],
]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

#感觉没什么亮点？只要把每个位置按他的前驱min算出来就好了


class Solution:
    def minPathSum(self, grid):

        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                print(dp[i][j])
                dp[i][j] = grid[i][j]
                if i > 0 and j > 0:
                    dp[i][j] += min(dp[i-1][j],dp[i][j-1])
                elif i > 0:
                    dp[i][j] += dp[i-1][j]
                elif j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[-1][-1]




print('ret:',Solution().minPathSum(grid))



#关于二维数组
# Note also that the copies are shallow; nested structures are not copied. This often haunts new Python programmers; consider:
#
# >>> lists = [[]] * 3
# >>> lists
# [[], [], []]
# >>> lists[0].append(3)
# >>> lists
# [[3], [3], [3]]
# What has happened is that [[]] is a one-element list containing an empty list, so all three elements of [[]] * 3 are (pointers to) this single empty list. Modifying any of the elements of lists modifies this single list. You can create a list of different lists this way:
#
# >>>
# >>> lists = [[] for i in range(3)]
# >>> lists[0].append(3)
# >>> lists[1].append(5)
# >>> lists[2].append(7)
# >>> lists
# [[3], [5], [7]]
# 也就是说matrix = [array] * 3操作中，只是创建3个指向array的引用，所以一旦array改变，matrix中3个list也会随之改变。
#

# m = 2
# n = 3
# new_grid = m*[n*[0]]
# print(new_grid)
# new_grid[0][0] = 12
# print(new_grid)
#
#
# m = 2
# n = 3
# new_grid = [[] for i in range(m)]
# print('new:',new_grid)
# new_grid[0].append(12)
# print(new_grid)
#
#
# test = [[0 for i in range(m)] for j in range(n)]
# print(test)





import time

length = 10000000

start = time.time()
l = []
for i in range(length):
    l.append(0)
end = time.time()
print('time1:',end - start)


start = time.time()
l = [0 for i in range(length)]
end = time.time()
print('time2:',end - start)


# 还是第三种最快，但是这种不能做成二维，二维的话就出问题了，所以第二种方法更常见？
start = time.time()
l = length * [0]
end = time.time()
print('time3:',end - start)












