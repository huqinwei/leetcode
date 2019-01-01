import math
from collections import deque
#给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
class Solution:
    # 简单的从大到小找能开方的数不能解决问题，12，减去9，还剩3，只能是3个1，总共是4，如果是3个4，更优。
    def numSquares_failed(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n
        cnt = 0
        while i > 0:
            print('i is {0},n is {1}'.format(i,n))
            sq = math.sqrt(i)
            if sq - sq // 1 == 0:#取模，相减，得到小数部分，看看小数部分是不是0，不是0就不是开方
                n -= i
                i = n
                cnt += 1
            else:
                i -= 1
        return cnt

    def numSquares_slow(self, n):
        # 超时了!猜测可能是分解成1+1+1这种占了时间？也不至于，不会走完它就提前结束了，主要还是分支太多？
        # 因为老是有这种简单的1+1占分支，一层比一层多。解决这个问题需要数学技能了吧
        # 好像也能用visited，没想好怎么用
        """
        :type n: int
        :rtype: int
        """
        dq = deque()
        dq.append(n)
        # dq.append(555)
        step = 0
        while dq:
            # print('size:',len(dq))
            for i in range(len(dq)):
                pop = dq.popleft()
                print('pop:',pop)
                if pop == 0:
                    return step
                for k in range(1,pop+1):
                    # print('k:',k)
                    if math.sqrt(k) - math.sqrt(k) // 1 == 0:
                        dq.append(pop-k)#每次减去一个完全平方和，存入余数，下一轮再拿余数做分解
            step += 1
    #############################################################
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = list()
        q.append([n, 0])
        visited = [False for _ in range(n+1)]
        visited[n] = True

        while any(q):
            num, step = q.pop(0)

            i = 1
            tNum = num - i**2
            while tNum >= 0:
                if tNum == 0:
                    return step + 1

                if not visited[tNum]:
                    q.append((tNum, step + 1))
                    visited[tNum] = True

                i += 1
                tNum = num - i**2


s = Solution()
print('ret:',s.numSquares(192))

