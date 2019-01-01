#  回文数
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？


# 当然不转字符串，转字符串那就成了判断字符串了，和数字有什么关系？
# 这题的思路应该是，只要是负数，就是false，正数的话，应该采用对折法，每次//10拿最高位，每次%10拿最低位，逐层对比
# 注意数字本身，这一回合下来应该是少了两位，尤其处理最后一次变化，如果剩0个，true，如果剩1个，true。剩两个的情况包含在正常循环里。

class Solution:
    def isPalindrome(self, x):#_myself
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 0
        y = x
        while y:
            count += 1
            y = y // 10
        # print('count:',count)
        count -= 1#乘以10的话，总位数减1

        while x and count:
            # 提取第一位用什么操作？只能自己算出来x有多少位？
            decimal = False#这是几十:x0的特殊处理.....或者另一个方法是先去尾部!!!!!
            if x >= 10:
                decimal = True

            up = x // 10 ** count
            x = x % 10 ** count
            # print('x:',x)

            if x == 0:
                if decimal:#这是几十:x0的特殊处理
                    return False
                return True
            down = x % 10
            x = x // 10
            # print('x:',x
            if up != down:
                return False
            count -= 2
            # print('while-loop count:',count)

        return True
    def isPalindrome_failed(self, x):#问题也不少
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 0
        y = x
        while y:
            count += 1
            y = y // 10
        print('count:',count)
        count -= 1#乘以10的话，总位数减1

        while x and count:
            down = x % 10
            x = x // 10
            if x == 0:
                return True
            print('down:',down)
            count -= 1#这个改法要注意count值的变化

            print('x:',x)
            print('count:',count)
            up = x // 10 ** count
            x = x % (10 ** count)#反向问题也不少。。。。x: 100002->x: 2
            print('up:',up)

            if up != down:
                return False
            count -= 1
            print('x:',x)

        return True

s = Solution()
print('ret:',s.isPalindrome(1000021))
