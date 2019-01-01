# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
#
# 案例:
#
# s = "leetcode"
# 返回
# 0.
#
# s = "loveleetcode",
# 返回
# 2.
#
# 注意事项：您可以假定该字符串只包含小写字母
import collections
class Solution:
    def firstUniqChar_myself(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1 = []
        set2 = []
        for i,c in enumerate(s):
            if c not in set2:
                if c not in set1:
                    set1.append(c)
                else:
                    set1.remove(c)
                    set2.append(c)
            else:
                continue
        # print('set1:',set1)
        if set1:
            for i,c in enumerate(s):
                if c == set1[0]:
                    return i
        else:
            return -1

    # 他这个算法利用了python的自建接口，算O(n ^ 2)了吧？除了接口内部有优化
    # def firstUniqChar(self, s):
    #     index = len(s)
    #
    #     for char in set(s):
    #         lindex = s.find(char)
    #         rindex = s.rfind(char)
    #         # 这里做-1检查是为了排除空字符串的特例
    #         if lindex == rindex:
    #             index = min(index, lindex)
    #     if index < len(s):
    #         return index
    #     return -1

    # 这个，没有顺序问题吗？
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = collections.Counter(s)
        print('dic:',dic)
        for i in range(len(s)):
            if dic[s[i]] == 1:#精髓在于访问的顺序，是按s中的字符顺序来控制的
                return i
        return -1



s1 = Solution()
ret = s1.firstUniqChar("loveleetcode")
print('ret:',ret)

# set1 = set()
# set1.add(1)
# print(set1)
# set1.remove(1)
# print(set1)
#
# l = [(1,'c'),(2,'c'),(3,'c'),(5,'d'),(1,'c'),]
# l.remove(1)
# print('l:',l)

s = 'hehehe'
print(s.find('h'))
print(s.find('e'))
print(s.rfind('h'))
print(s.rfind('e'))

dic = {}
print(dic)
dic['e'] = 1
print(dic)
dic['d'] = 1
print(dic)
dic['e'] += 1
print(dic)
dic['f'] = 1
print(dic)
dic['h'] = 1
print(dic)