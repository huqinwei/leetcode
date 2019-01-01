#  买卖股票的最佳时机
# 题目描述提示帮助提交记录社区讨论阅读解答
# 随机一题
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


# 只有一次交易，光找到min和max还不行，还要保证顺序，是保证min在max之前的前提下的max-min，有点动态的感觉
#[5,6,1,4]
class Solution:
    def maxProfit_false_mod(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_ = prices[0]
        max_ = prices[0]
        profit = []
        for i in prices:
            # print(i)
            if i < max_:
                profit.append(max_ - min_)
                min_ = i
                max_ = i
            max_ = i
        profit.append(max_ - min_)
        profit.sort()
        return profit[-1]
        # 这样改也不对，还是按局部落差来算的，实际上可以跨越局部，只要min在max左边就行

    # 思路是这样，存一个max的dict，从一个min的dict，还要有下标。
    # 从max中拿一个下标，和min比左右，不行就再换一个max，不行就再换一个min。
    # 如果dict中数值相等呢？取舍，min就留左边的，max就留右边的？dict中怎么按大小或者顺序取值？
    #

    # 先用O(n2）解吧,明显的要超时
    def maxProfit_overtime(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        n = len(prices)
        min_ = prices[0]
        max_ = prices[0]
        profit = []
        for i in range(n):
            for j in range(i,n):
                if prices[i] < prices[j]:
                    profit.append(prices[j] - prices[i])
        profit.sort()
        return profit[-1] if len(profit) else 0


# 像水桶的，却不知道如何用
# 水桶是为了两个边都很高，然后用面积来判定，面积不是绝对，如果不算长度，这个算法也成立。本例是需要一边低一边高，不成立。



# 实际答案：不维护最大，只维护最小，因为迭代器是向前走的，所以当前值减去最小永远是最大利润，维护最大利润就好了。
    def maxProfit(self, prices):

        max_profit = 0
        if prices == []:
            return max_profit
        min_price = prices[0]
        for i in range(len(prices)):
            # if prices[i] > min_price:#不需要if，本来是个max更新操作
            max_profit = max(max_profit,prices[i]-min_price)
            min_price = min(min_price,prices[i])

        return max_profit
s = Solution()
print('ret:',s.maxProfit([7,6,4,3,1]))


# dict = {3:'a',4:'b',5:'c'}
# print(dict)
# dict.
# print(dict)

