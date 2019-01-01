from collections import Counter


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 可以使用字典        dict        来记住这些字符对是一个很方便的做法。在这里面我用了两个字典dict，
        # 一个字典        hashmap        用来记        s        的字符到t        的映射，
        # 另一个字典        ismap        用来记录        t        的字符到s        的映射，
        # 用于判断        t        中的两个字符不能由        s        中同一个字符映射而来。
        # 说人话：s: egggf和t:addcd。s2t映射存的是供查询用的字母映射：e->a, g->d
        # i = 0, 插入e:a，对面插入a已被占用
        # i = 1, 插入g:d，对面插入d已被占用
        # i = 2, 再出现g的时候，先看存没存映射，存了就看内容，是d，对面t中是d，仍然符合，下一轮！
        # i = 3, 再出现g的时候，内容是d，对面是c，不符合，False
        # i = 4,（假设i = 3没退出），f是新的，想插入f: d，查询对面t中是否已存在d，存在，冲突，False。
        hashmap = {}
        ismap = {}
        for i in range(len(s)):
            print('s[i]:',s[i])
            print('t[i]:',t[i])
            if s[i] not in hashmap:
                print('not in')
                if t[i] in ismap:
                    return False
                hashmap[s[i]] = t[i]
                ismap[t[i]] = s[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return True


s = "eggf"
t = "addd"



print(dict)

s1 = Solution()
ret = s1.isIsomorphic(s, t)
print('ret:',ret)

s = "egge"
t = "aaff"
c1 = Counter(s)
c2 = Counter(t)
print(c1)
print(c2)
print(c1[0])
print(c1['e'])
for i in range(len(s)):
    # print(i)
    print(s[i] in c1)
    print(t[i] in c2)
    print(c1[s[i]])
    print(c1[s[i]])
# 只计数肯定不行，因为只是计数，顺序也是不能保存下结构:
# s = "egge"
# t = "aaff"
# Counter({'e': 2, 'g': 2})
# Counter({'a': 2, 'f': 2})
# 两个字符不能映射到同一个字符上，但字符可以映射自己本身。这句话，中文能解释清么？意思是e和g不能都映射到新的a,要用a和b


print('############################################################################')
print('############################################################################')

####################################################################
#set and dict demo

#type
dict1 = {4:'444'}
set1 = {4}
print(type(dict1))
print(type(set1))

####################################################################
#set demo
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('pineapple' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)

print(a-b)
print(b-a)
print(a&b)
print(a|b)
print(a^b)#  equals to a-b  +  b-a
print((a-b)|(b-a))
print((a-b)|(b-a) == a^b)

a = {x for x in 'abracadabra' if x not in 'a'}
print(a)
a = {x for x in 'abracadabra' if x not in 'ab'}
print(a)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

set1 = set(("google","baidu","soga"))
set1.add('apple')
print(set1)
set1.add('google')
print(set1)
set1.update(('pineapple'))###########################################11111!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(set1)
set1.remove('apple')
print(set1)
set1.discard('apple')
print(set1)
pop1 = set1.pop()#randomly
print(set1)
print(pop1)
print(len(set1))
print('google' in set1)
set1.clear()
print('google' in set1)
print(set1)


nums1=set((1,2,2,1))
print(sum(nums1))
# print((nums1)**2)


print('############################################################################')

####################################################################3
#dict demo

dict1 = {'alice': '2341', 'Beth':'9102', 'Cecil':'3244', 1:'3311'}
print(dict1)
print(dict1['alice'])
print(dict1[1])

# print(dict1[0])#error
dict1[0] = '4322'
print(dict1[0])

print('before del:',dict1)
del dict1[0]
print('after del:',dict1)
# print(dict1[0])#error

dict2 = {'alice':'2345', 'bob':'1234', 'alice':'8888'}
print(dict2)
print(len(dict2))
print(str(dict2))
print(type(str(dict2)))
print(set(dict2))
print(type(set(dict2)))
# dict2 = {'alice':'2345', 'bob':'1234', 'alice':'8888',['hog']:'9887'}#TypeError: unhashable type: 'list'

print('alice' in dict2)
print(dict2.get('1234'))
print(dict2.get('alice'))

print(dict2['bob'])
# print(dict2['cc'])

print(dict2.get('cc'))
print(dict2.get('bob'))


bbb = {}
print(type(bbb))












