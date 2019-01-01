# from string import replace
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        s1 = list(s)
        # print(type(s1))
        n = len(s)
        p = 0
        q = n - 1
        vowels = 'aeiouAEIOU'

        while p < q:
            print('p is ',p,' q is ',q)
            if not s1[p] in vowels:
                p += 1
                continue
            if not s1[q] in vowels:
                q -= 1
                continue

            s1[p],s1[q] = s1[q], s1[p]


            p += 1
            q -= 1
        # 主要问题就是怎样返回字符串形式，这种不行：return str(s1)
        return ''.join(s1)


s = ['h','e','l']
s2 = str(s)
print('s2:',s2)
# s[0],s[1] = s[1],s[0]
# print(s)
str1 = 'hello'#TypeError: 'str' object does not support item assignment
print(type(str1))
print(type(str1[2]))
print(str1[2])

# str1 = '1232245'
# str1 = str1[2].replace("3","8",1)
# print('after replace:',str1)


# str1 = ['h','e','l','l','o']
print(str1)
s1 = Solution()
s = s1.reverseVowels(str1)
print('ret:',s)


