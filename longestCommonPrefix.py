# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#

# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

# 思路：
# 记住总长度n，第一个单词，生成k个字典，后边的类似，+=1，最后看总长度
# 从第一个单词按顺序查字典，如果够长，就算，就给扔到ret
# 这样是有问题的，字母总归有重复，碰到sss ccc， zzz，难道因为s有三个，就说第一个s是公共的？
# 第一个整个用index-value存下来，其他的用index访问value对比
class Solution:
    def longestCommonPrefix_myself(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        dict = {}
        common = len(strs[0])
        for i,s in enumerate(strs):
            count = 0
            # print('i:{0},s:{1}'.format(i,s))
            for j,c in enumerate(s):
                # print('j:{0},c:{1}'.format(j,c))
                if count >= common:
                    break
                if dict.get(j) == None:
                    if i == 0:#init
                        dict[j] = c
                        count += 1
                    else:
                        break
                else:
                    if dict.get(j) != c:
                        break
                    count += 1

                dict[j] = c
                # print('count:',count)
            common = count
            # print('common:',common)
        ret = ''
        for i in range(common):
            ret += dict[i]
        return ret

    # 这个直接用了min和max，用min去max找，找对几个是几个
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        print(strs)
        s1 = min(strs)
        s2 = max(strs)
        print('s1:',s1)
        print('s2:',s2)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

    # 他这说白了就是横向对比，逐个下标去对比
    def longestCommonPrefix_heng(self, s1):
        """
        :type strs: List[str]
        :rtype: str
        """
        if '' in s1 or s1 == []:
            return ''
        elif len(s1) == 1:
            return s1[0]
        else:
            min_len1 = min(len(s) for s in s1)
            flag = 0
            for j in range(min_len1):#他的意思是，找出最短长度，每次拿一个下标去访问所有单词
                for i in range(len(s1) - 1):
                    if s1[i][j] == s1[i + 1][j]:
                        print('i:{0},j:{1},flag:{2}'.format(i,j,flag))
                        if i == len(s1) - 2 and flag >= j:  ##这行代码很重要
                            flag += 1# 这个判断逻辑的精髓是如果i能走到倒数第二个，那么这第j个字母，就算是所有单词共有了。
                    else:# 不相同的就直接break了，相同的再看是不是倒数第二个单词？如果是，再去加flag。
                        break
            if flag > 0:
                return s1[0][:flag]
            else:
                return ""


strs = ["flower","flow","flight"]
# strs = ["aaa","aa","aaa"]
# strs=["c","acc","ccc"]
strs=["flowww","flowwv","flox"]
s = Solution()
print(s.longestCommonPrefix(strs))




