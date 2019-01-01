#   字符串相乘
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。


# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

# 思路，不能直接转换为整数，那他的意思应该是自己实现乘法规则，逐位最小乘法，然后做加法？
# 也不行的，长度110，用num1的一位去乘以num2整个也不行
# 应该是利用逻辑，把每一位算出来，算出一个进位，这个进位肯定不会超。


# 数学算法总结，假如最后一位[n-1]是0！！！！！
# 结果的最后一位res[0]是num1[0]*num2[0],倒数第二位res[1]是前边的carry+num1[1]*num2[0] + num1[0]*num2[1]，
# 总之，res[i]是num1和num2下标总和等于i的所有总和加上之前的进位，结果的个位数。
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        res = ''
        carry = 0
        m = len(num1) - 1
        n = len(num2) - 1
        for k in range(m + n + 1):
            # print('k:',k)
            sum = carry
            for i in range(k+1):
                j = k - i
                if i <= m and j <= n:
                    # print('i:{0},j:{1}'.format(i,j))
                    index_i = m - i
                    index_j = n - j
                    sum += int(num1[index_i]) * int(num2[index_j])
            res = str(sum % 10) + res
            carry = sum // 10
            # print('carry:',carry, ' sum:',sum)

        if carry:
            res = str(carry) + res
        return res
        # print('res:',res)
num1 = "123"
num2 = "456"# 输出: "56088"
s = Solution()
s.multiply(num1,num2)

