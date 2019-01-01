from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        # dict1 = dict()
        # # ret = []
        # for i in range(len(s)):
        #     k = s[i]
        #     if dict1.get(k) != None:            #if k in dict1:
        #         dict1[k] = dict1[k] + 1
        #     else:
        #         dict1[k] = 1
        # print(dict1)
        # for j in range(len(t)):
        #     k2 = t[j]
        #     if k2 in dict1:
        #         dict1[k2] -= 1
        #         # ret.append(k2)
        #         if dict1[k2] == 0:
        #             del(dict1[k2])
        #     else:
        #         return False
        #
        # if dict1 != {}:
        #     return False
        # return True

        c1 = Counter(s)
        print('c1:',c1)
        c2 = Counter(t)
        print('c2:',c2)
        print(type(c2))
        if c1 == c2:
            return True
        return False



s = "ab"
t = "a"

# for i,num in enumerate(nums1):
#     print('{0},{1}'.format(i,num))

print(dict)

s1 = Solution()
ret = s1.isAnagram(s, t)
print(ret)


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


#counter is orderless
#没什么顺序而言，各个Counter还巧合的连打印出来也一样。
c1 = Counter("abc")
print(c1)
c2 = Counter("cba")
print(c2)
print(c1 == c2)
print(id(c1) == id(c2))

