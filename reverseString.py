# 反转字符串
# 编写一个函数，其作用是将输入的字符串反转过来。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "olleh"
# 示例 2:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: "amanaP :lanac a ,nalp a ,nam A"

class Solution:
    def reverseString_myself(self, s):
        n = len(s)
        ret = ''
        for i in range(n-1,-1,-1):
            ret+=s[i]
        return ret

    # 看起来，这种强转list，翻转list，再一次性接到string的方法更快，可能list的翻转确实更有优势，join的过程估计也被优化过了。肯定不是按遍历走的。
    def reverseString(self, s):
        li=list(s)
        print(li)
        li.reverse()
        print(li)
        ostr="".join(li)
        return ostr

    # 这。。。。
    # def reverseString(self, s):
    #     return s[::-1]
s = Solution()
print(s.reverseString('hello.worl!d'))
print('hhhaa'[::-1])












