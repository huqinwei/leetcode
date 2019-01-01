class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # squares = n
        # while squares >= 10:
        #     tmp = 0
        #     while squares:
        #         tmp += (squares % 10) * (squares % 10)
        #         squares = squares // 10
        #     squares = tmp
        # if squares == 1 or squares == 7:
        #     return True
        # return False

        # 判断出现的数之前有没有出现过，出现过就会产生循环，就不是快乐数。可以用集合set来记录之前出现的数字。
        # 重复就不行？那么一直变大不重复行不行？这题太数学了，忽略数学意义分析！
        # 999得到243, 可能确实不会无限变大，又因为如果得到重复的数，后边的过程肯定还能循环回来，好像可以证明
        # 输入虽然可以随机，比如9999，但是终究还是要收敛回来
        ss = set()
        while True:
            if n == 1:
                return True
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n = n // 10

            print('tmp:',tmp)
            if tmp in ss:
                return False

            ss.add(tmp)
            n = tmp

s1 = Solution()
ret = s1.isHappy(119)
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







