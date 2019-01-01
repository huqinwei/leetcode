


# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。


coins = [1, 2, 5]
amount = 11
# 输出: 3



# coins = [2]
# amount = 3
# 输出: -1


# 之前有个题是用多少张什么币拼出一个指定金额，贪心，但是那个简单在于每种面额你都可以无限用
# 这里其实也没限制数量，但是面额是给出的，之前固定就是100,50,20之类的，现在可能有100可能没100，都没准，那么我排个序不就好了？为什么是DP？
# 唯一不同的是可能拼不出来？

coins = [186,419,83,408]
amount = 6249

#预期结果20



class Solution:
    # 问题出现了，面额很不规整，可能实际能拼凑出来，只是拼凑的规则不是那样从大到小，越大越优先。
    # 之前好像提到过，如果出现7块钱，结果就不同了，这里也是，数字间并不遵从2倍+关系。
    # 再举个栗子，2,99,100，现在101，会优先去找100，结果成了无解
    def coinChange_failed(self, coins, amount):
        coins.sort(reverse=True)
        total_coins = 0
        print(coins)
        for i in range(len(coins)):
            print(amount)
            if amount // coins[i]:
                total_coins += amount // coins[i]
                amount = amount % coins[i]
        # print(amount)
        if amount:
            return -1
        return total_coins

    #感觉更像火柴拼方框的思路，从大到小，逐渐往里边试
    # 但是和火柴不同的是，火柴每一样都有数的，可以DFS，这个每一样都是无限的，也直接DFS？然后超出的剪枝？
    # 期望20，输出了26，并且leetcode超时@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!!!!!!!!!!!!!!!!!!!!!!!!!!!.
    # 我这个算法，可能能找到结果，但是不是符合条件的结果——“最少用多少张”。!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 我这是碰到什么算什么，再费劲去对比也没用了，本来就超时了，再拿更多结果，肯定超了
    def generate(self,coins,target,bucket,total):#target和bucket可以合并功能，先不管！
        # print('call generate:bucket:',bucket,' target:',target)
        if bucket == target:
            return total
        if bucket > target:
            return -1
        for x in coins:
            # print('x:',x)
            ret = self.generate(coins,target,bucket+x,total+1)
            if ret != -1:
                return ret
        return -1

    def coinChange_failed2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        total_coins = 0
        # print(coins)

        # print(amount)
        bucket = 0
        return self.generate(coins,amount,bucket,0)


    # 这个，给 出答案很容易理解，但是自己想很难想啊，尤其是这不同的面额，光是有想法，怕是都不好想怎么实现，因为这里边很多空的情况
    #这个等于每一步往前依赖m步，m是coins的数量，而且依赖的还分空和有值的情况
    def coinChange(self, coins, amount):
        n = len(coins)

        dp = (amount+1) * [-1]
        dp[0] = 0

        for i in range(1,amount+1):

            for coin in coins:
                if coin <= i and dp[i-coin] != -1:#如果这个面额不超过i，证明可以用来拼凑。并且要用来拼凑的dp对应位不是空的！则准备拼凑！
                    if dp[i] == -1 or dp[i] > dp[i-coin] + 1:#这是个更新过程，如果这是第一次，那肯定要更新，或者不同的面额也要试探着来,这个dpi并没有新得到的优，就更新，这块是求min
                        dp[i] = dp[i-coin]+1
        return dp[-1]




sol = Solution()
print('ret:',sol.coinChange(coins,amount))






