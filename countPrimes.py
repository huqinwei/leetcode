#   计数质数
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。


# 一个思路是，逢2、3、5的倍数就跳过去，从根本上减少需要循环检测的数据
# if (i > 2 and i % 2 == 0) or (i > 3 and i % 3 == 0) or (i > 5 and i % 5 == 0) or (i > 7 and i % 7 == 0):
# 还是蠢，还是慢！
import math
class Solution:
    def countPrimes_overtime(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []#换成字典并不能解决问题，终归要遍历的，字典访问也是O(1)，下标访问也是O(1)
        if n < 3:
            return len(primes)
        for i in range(2,n):
            j = 0
            m = len(primes)
            while j < m:
                if i % primes[j] == 0:
                    break
                j += 1
            if j == m:
                primes.append(i)
            print(primes)
        return len(primes)

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        #primes = []#换成字典并不能解决问题，终归要遍历的，字典访问也是O(1)，下标访问也是O(1)
        sum = 0
        if n < 3:
            return sum
        for i in range(2,n):
            if i == 2 or i == 3:
                sum += 1
                continue
            # print('================i:',i)
            sqrt_i = int(math.sqrt(i))
            # print(' sqrt_i+1:',sqrt_i + 1)
            for j in range(2, sqrt_i+1):
                # print('j:',j,' sqrt_i+1:',sqrt_i + 1)
                if i % j == 0:
                    break
                if j == sqrt_i:
                    # print('prime')
                    sum += 1
        return sum


    # def countPrimes(self,n):
    #     import math
    #
    #     count=0
    #
    #     def judge_prime(w):
    #         sqrt_w=int(math.sqrt(w))
    #         for i in range(2,sqrt_w+1):
    #             print('i:',i,' x:',x,' sqrt_w+1:',sqrt_w+1)
    #
    #             if x%i==0:
    #                 return 0
    #         return 1
    #
    #     for x in range(2,n):
    #
    #         count=count+judge_prime(x)
    #     return count

# def countPrimes(self, n):
#     if n < 3:
#         return 0
#     primes = [True] * n
#     primes[0] = primes[1] = False
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
#     return sum(primes)
# ---------------------
# 作者：二当家的掌柜
# 来源：CSDN
# 原文：https://blog.csdn.net/github_39261590/article/details/73864039
# 版权声明：本文为博主原创文章，转载请附上博文链接！
# class Solution {
# public int countPrimes(int n) {
# int count = 0;
#
# boolean flag[] = new boolean[n]; // 初始全都false
#
# for (int i = 2; i < n; i++)
# if (flag[i] == false){
# count ++;
# for (int j = 1; j * i < n; j++)
# flag[j * i] = true;
# }
#
#
# return count;
# }
# }



s = Solution()
print(s.countPrimes_overtime(100))


# print(10%5)
# print(6%10)

# dic = {5:3,6:5}
# print('l:',len(dic))
# for i in dic:
#     print(i)
#     print(dic[i])