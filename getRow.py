#   杨辉三角 II
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 空间复杂度可以优化，找到规律以后，改成每次改变数组，应该就可以。。。

class Solution:
    def getRow_myself(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        if not rowIndex:
            return None
        res = [[0] * (i+1) for i in range(rowIndex)]
        # print(res)
        for k in range(rowIndex):
            for i in range(k+1):
                if res[k-1] and i == 0 or i == len(res[k])-1:
                    res[k][i] = 1
                elif res[k-1]:
                    res[k][i] = res[k-1][i-1] + res[k-1][i]
        print(res)
        return res[-1]
    def getRow_myself2(self, rowIndex):#myself   v2
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        if not rowIndex:
            return None
        res = [0] * rowIndex
        # print(res)
        for k in range(rowIndex):
            temp = 0
            for i in range(k+1):
                temp1 = res[i]#重点在这个temp，原则上是拿前一行的[i-1]+[i]，但是本行[i-1]已经改写完了，所以必须缓存前一行[i-1]。
                if i == 0:
                    res[i] = 1#include initialize
                elif i == k:
                    res[i] = 1
                else:
                    # res[i] = res[i-1] + res[i]
                    res[i] = temp + res[i]
                temp = temp1
            # print(res)
        # print(res)
        return res

    # 别人的简洁写法
    def getRow(self, rowIndex):
        if rowIndex==0:
            return [1]
        l=[1]
        n=1
        while True:
            l.append(0)#他的核心技巧就在那个[-1]是append的0！！
            print('n:',n)
            print('before:',l)
            l=[l[i]+l[i-1] for i in range(n)]#他这个方法很简洁，-1居然也不越界，可奇怪的是，[0]+[-1]居然没成2！因为先append了个0！
            print('after:',l)
            n+=1
            if n>rowIndex+1:
                return l
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]
        for i in range(rowIndex+1):
            res.append(1)
            for j in range(i-1,0,-1):
                res[j]=res[j-1]+res[j]
        del(res[-1])
        return res

s = Solution()
print('ret:',s.getRow(4))
