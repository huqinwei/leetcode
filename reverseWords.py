#   翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 示例:
#
# 输入: "the sky is blue",
# 输出: "blue is sky the".
# 说明:
#
# 无空格字符构成一个单词。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
# 进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。

class Solution(object):
    def reverseWords_myself(self, s):
        # 因为最后一个单词后边不能加空格，如果无差别递归的话最后一个单词后有空格。
        # 不能自己改函数参数，哪怕加默认值也不可以，那就不能拿外层递归了，自己写一个递归函数。
        def reverseWordsInner(s,is_first = True):
            n = len(s)
            res = ''
            if n == 0:
                return res
            # print(s)
            # print(s[1:])
            i = 0
            while i < n and s[i] == ' ':
                # print('i:',i)
                i += 1
            if i == n:#消除后边的空格
                return res
            while i < n and s[i] != ' ':
                # print('i:',i)
                res += s[i]
                i += 1
            # if i != n:
            #     res += ' '
            if not is_first:
                print('not first')
                res += ' '
            print('res:',res)
            return reverseWordsInner(s[i:],False) + res

        return reverseWordsInner(s,True)

    # 思路2，整个字符串变字符数组，翻转，每个单词内部翻转。当然，还得处理空格。

    # 别人都是split成了单词的数组，然后reverse数组
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return ""
        s = s.strip().split(" ")
        print(s)
        new = [i for i in s if i != ""]
        if not new:
            return ""
        new.reverse()
        return " ".join(new)
strs = "the sky is blue"
# strs = " 1 "

s = Solution()
print('ret:',s.reverseWords(strs))

