#   字母异位词分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
import collections
class Solution:
    def groupAnagrams_v1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        # print(ans)
        print(ans.values())
        print(type(ans.values()))
        print([ans.values()])
        print(type([ans.values()]))
        # print(ans.values().__contains__())
        # return ans.values()
        return ans.values()#最后，dict_values返回，在leetcode的python3还不认，python认。python3得找一个转化手段。


    def groupAnagrams(self, strs):
        if len(strs) == 0:
            return []
        ret = []
        memo = {}
        k = 0
        for s in strs:
            # print(s)
            # print(sorted(s))
            # print(tuple(sorted(s)))
            if tuple(sorted(s)) not in memo:
                memo[tuple(sorted(s))] = k
                ret.append([])
                k+=1
            ret[memo[tuple(sorted(s))]].append(s)
            print(ret)
        return ret

        # def groupAnagrams(self, strs):
        #
        # if len(strs) == 0:
        #     return []
        # ret = []
        # memo = {}#memo的映射是一个排好序的字母组合key和一个无关紧要的排序k做value
        # k = 0
        # for s in strs:
        #     #preprocessing
        #     ls = list(s)
        #     # print('ls:',ls)
        #     ls.sort()
        #     # print('sort:',ls)
        #     only_one = ''.join(ls)
        #     #only one:
        #     if only_one not in memo:#only_one是转化后的，具有唯一性，不同的词可能是同一个only_one
        #         memo[only_one] = k#k是memo的下标，迭代递增，k不用有n那么长，他是有一个新的key才给k自增.tone其实就是key了
        #         k += 1
        #         ret.append([])
        #     ret[memo[only_one]].append(s)#memo[only_one] == k - 1#其实是有关系的，每次k增1，ret也append一个list，所以，他用了memo的value做ret的索引
        # return ret


#还有一种映射方法，就是用类似onehot的方法，每个字母对应的出现次数存起来，一个数组26个，每一种不同的组合对应一个key，太多了吧？无所谓，反正都封装了，其他的也这样啊

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print('ret:',s.groupAnagrams(strs))



# ans = collections.defaultdict(list)
# ans2 = collections.defaultdict(list)
# ans3 = collections.defaultdict(list)
# for s in strs:
#     print('s:',s)
#     print(sorted(s))
#     print(tuple(sorted(s)))
#
#     ans[tuple(sorted(s))].append(s)
#     #ans2[(sorted(s))].append(s)#unhashable type: 'list'
#     ans2[(tuple(s))].append(s)
#     ans3[((s))].append(s)
# print(ans)
# print(ans.values())
# print('ans2:',ans2)
# print('ans2:',ans2.values())
# print('ans3:',ans3)
# print('ans3:',ans3.values())
