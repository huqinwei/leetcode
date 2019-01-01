class Solution:
    def maxProfit_myself(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_ = prices[0]
        max_ = prices[0]
        acc = 0
        for i in prices:
            # print(i)
            if i < max_:
                acc += max_ - min_
                min_ = i
                max_ = i
            max_ = i
        acc += max_ - min_
        # print('acc:',acc)
        return acc
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        acc = 0
        if len(prices) <= 1:
            return acc
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                acc += prices[i] - prices[i-1]
                print('acc:',acc)

        return acc



s = Solution()
print('ret:',s.maxProfit([7,1,5,3,6,4]))