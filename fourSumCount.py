#   四数相加 II
# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
#
# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
#
# 例如:
#
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
#
# 输出:
# 2
#
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0



# 大概思路有：
# 用不同的哈希表分别存组合，然后拿出来拼。
# 把负数的组合和整数的组合分开，直接去对面找个互补的就行了。
# 既然要的是0，正数就肯定要和负数组合，四个零单独处理就好了。
# 但是这个思路是普通的4sum，现在的是，从四个列表分别拿出
# 这样反而更简单了？
# 如果把i和j的和做一个key，同一个key可以有不同的组合达成吧。
# 虽然只问你有多少组，没问你具体的数值，但是-1,1组成的0和-2,2组成的0绝对是两个。

class Solution:

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic1 = {}
        cnt = 0
        for i in A:
            for j in B:
                dic1[i+j] = dic1.get(i+j,0) + 1
                print('dic1:',dic1)
        for i in C:
            for j in D:
                complement = 0 - i - j
                cnt += dic1.get(complement,0)
                print('cnt',cnt)
        return cnt
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
s = Solution()
print(s.fourSumCount(A,B,C,D))



# d = {}
# d[3]=54
# print(d)
# print(d.get(3))
# print(d.get(3, 0))
# print(d.get(3, 1))
# print(d.get(5))
# print(d.get(5,0))#如果没有，返回的是0，方便直接0变1
