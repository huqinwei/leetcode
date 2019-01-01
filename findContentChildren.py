#这个人民币的贪心算法是有前提条件的，面值有严格的二倍以上的关系
#如果有7块的，14就是两张7，但是10+2+2是三张
#
# RMB = [100,50,20,10,5,2,1]
# value = 628
# count = 0
# for x in RMB:
#     use = value // x
#     print('use:',x,use)
#     count += use
#     value -= x*use
#     print('value:',value)
# print(count)








# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；
# 并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
# 你可以假设胃口值为正。
# 一个小朋友最多只能拥有一块饼干。
#
# 示例 1:
#
# 输入: [1,2,3], [1,1]
#
# 输出: 1
#
# 解释:
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。

class Solution:
    # def findContentChildren_other(self, g, s):
    # 没明白，这是从最小的开始满足吗？可能是这意思，虽然满足小的剥夺了大的机会，但是只看满足人数，可能没区别。
    # 如果说满足的情况下浪费的情况更少，我觉得肯定得从大算起了？如果只看满足数量，从小也可以！
    #     result = 0
    #     sorted_g = sorted(g)
    #     sorted_s = sorted(s)
    #     i, j = 0, 0
    #     while i < len(sorted_g) and j < len(sorted_s):
    #         if sorted_g[i] <= sorted_s[j]:
    #             result += 1
    #             i += 1
    #             j += 1
    #         else:
    #             j += 1
    #     return result

    def findContentChildren_myself(self, g, s):#本质区别不是从大到小还是从小到大，我这种方法可能是O(n^2)，他那是O(n)，本质在于我没有同步遍历
        count = 0
        g.sort()
        s.sort()

        for i in range(len(g)-1,-1,-1):
            print(i)
            for j in range(len(s)-1,-1,-1):
                if s[j] >= g[i]:
                    count += 1
                    del s[j]
                    break
        return count

    def findContentChildren(self, g, s):
        count = 0
        g.sort()
        s.sort()

        i = len(g) - 1
        j = len(s) - 1
        while i>=0 and j>=0:
            if g[i] <= s[j]:
                count +=1
                j-=1
            i-=1

        return count



g = [1,2]
s = [1,2,3]
# 输出: 2

sol = Solution()
ret = sol.findContentChildren(g,s)
print(ret)














