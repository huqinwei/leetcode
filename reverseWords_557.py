#   反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc"
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution:
    def reverseWords_myself(self, s):#use api
        strs = s.split(' ')
        res = ''
        print(strs)
        for i,k in enumerate(strs):
            kk = list(k)
            l = 0
            r = len(kk) - 1
            while l < r:
                tmp = kk[l]
                kk[l] = kk[r]
                kk[r] = tmp
                l += 1
                r -= 1
            # print('kk:',kk)
            temp = ''.join(kk)
            res += temp
            if i != len(strs) - 1:
                res += ' '
            # print('res:',res)
        # print(list)
        return res

    def reverseWords_v2(self, s):
        s_lst = s.split(' ')
        output_s = ''
        for x in s_lst:
            output_s += (x[::-1] + ' ')

        return output_s[:-1]#利用[:-1]把多余的空格删掉

    # 熟练的转换，还有join的用法
    def reverseWords(self, s):
        print(s[::-1])
        print(s[::-1].split())
        print(s[::-1].split()[::-1])
        print(' '.join(s[::-1].split()[::-1]))
        return ' '.join(s[::-1].split(' ')[::-1])

strs = "Let's take LeetCode contest"

s = Solution()
print('ret:',s.reverseWords(strs))

# l2 = ['a','e','d']
# s2 = str(l2)
# print('s2:',s2)




