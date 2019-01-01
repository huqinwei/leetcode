class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
            # print(s)
        return False


        # return len(set(nums)) < len(nums)


s1 = Solution()
ret = s1.containsDuplicate([1,2,3,4,3])
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

del dict1[0]
print(dict1)
# print(dict1[0])#error

dict2 = {'alice':'2345', 'bob':'1234', 'alice':'8888'}
print(dict2)
print(len(dict2))
print(str(dict2))
print(type(str(dict2)))
print(set(dict2))
print(type(set(dict2)))
# dict2 = {'alice':'2345', 'bob':'1234', 'alice':'8888',['hog']:'9887'}#TypeError: unhashable type: 'list'







