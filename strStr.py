#   实现strStr()
# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


class Solution:
    def strStr_myself(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            k = i
            if (len(haystack) - k) < len(needle):
                return -1
            for j in range(len(needle)):
                if haystack[k] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
                k += 1

        return -1
    def strStr(self, haystack, needle):

        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0]:
                j = 1       #j = 0#放心，没问题，从1开始
                while j < len(needle) and haystack[i+j] == needle[j]:
                    j+=1        #如果接下来相等，则j不断增加
                if j == len(needle):
                    return i
        return -1
        #相当于是python中find的底层应用
        #可以循环，找到第一个相同的字母，记录下位置i和新的下标j，然后逐一对比是否相同
        #因为找第一个位置，因此就只循环长-短的就好
        #首先判断特殊情况

s = Solution()
# print('ret:',s.strStr(haystack = "helllllo", needle = "llo"))
print('ret:',s.strStr(haystack = "", needle = "a"))

str1 = 'hllla'
str2 = 'lla'
print(str1.find(str2))









