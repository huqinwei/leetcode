#  x 的平方根
# 实现 int sqrt(int x) 函数。
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 示例 1:
# 输入: 4
# 输出: 2
# 示例 2:
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。


# 优化：超过4以后，应该right直接用x // 2就够吧。,废话，超过9还能用x//3呢.所以说，可以动态的用x的平方根？但是你找的就是平方根，找到了就不用搜了!!
# 利用平方计算？mid ** 2,大于x算结束？保留之前的不大于x的mid，那用什么二分查找啊？
# 那就先把各iter平方和都存起来？有这个复杂度，还用什么二分查找？直接从头到尾遍历，直到平方大于等于x，那多好？#提交结果：超出时间限制!!!!!!!!!!!!!

# 整体思路是循环找不到小数，对小数结果的边界进行处理
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        mid = 1
        while left <= right:
            # print('left:{0},right:{1}'.format(left,right))
            mid = (left + right) // 2#left + (right - left) // 2
            # print('mid:',mid)
            if x // mid == mid:
                return mid
            elif x // mid > mid:
                left = mid + 1
            else:
                right = mid - 1
        # print('finish:left:{0},right:{1}'.format(left,right))

        #return mid    finish:mid: 3 left:3, right: 2 return 3
        return right
        # 为什么拿right，找到最后没找到，说明真实的小数处于right和left之间。因为现在已经right小于left了，所以拿right。
        # 结束前left==right，结束时无论是right-=1还是left+=1，取更小的那个整数，都是right，而如果用mid的话，最后一步是right-1就完了

    # def mySqrt(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     return int(x ** (1/2))

    # def mySqrt_slow(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     sqrt = 0
    #     while sqrt < x:
    #         if (sqrt+1)**2 >x:
    #             return sqrt
    #         sqrt+=1
    #     return sqrt


s = Solution()
print(s.mySqrt(7))






