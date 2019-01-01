class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        p = 0
        q = n - 1
        # 'A' to 'Z'
        # 'a' to''z'
        # 'A' == 'a'
        # '0' to '9'
        # is number  or is character
        while p < q:
            # print('p is ',p,' q is ',q)
            if not s[p].isalnum():
                p += 1
                continue
            if not s[q].isalnum():
                q -= 1
                continue
            if s[p].capitalize() == s[q].capitalize():
                p += 1
                q -= 1
            else:
                return False
        return True

    def isPalindrome_v2(self, s):
        s = s.lower()
        character = 'abcdefghijklmnopqrstuvwxyz0123456789'
        # is number  or is character
        l = []
        for i in s:
            print('i:',i)
            if i in character:
                l.append(i)
                print('l:',l)
        print('l is ',l)
        print('l[::-1] is ',l[::-1])
        if l == l[::-1]:
            return True
        return False
    def isPalindrome_v22(self, s):
        s = s.lower()
        character = 'abcdefghijklmnopqrstuvwxyz0123456789'
        # is number  or is character
        l = []
        for i in s:
            print('i:',i)
            if i in character:
                l.append(i)
                print('l:',l)

        #这样遍历是比不过l==l[::-1]的
        left = 0
        right = len(l)-1
        while left < right:
            if l[left] != l[right]:
                return False
            left += 1
            right -= 1
        return True



str = "A man, a plan, a canal: Panama"
print(str)
print(len(str))

print(str[0])
print(str[0] > 'a')
print('c' > 'b')
print('a' > 'b')
print('A' > 'a')
print('Z' > 'a')
print('a' < 'z')

print(str[0].isalpha())
print(str[1].isalpha())
print(str[5].isalpha())
print('a'.isalnum())
print('a'.capitalize())
print('3'.capitalize())
print('3'.isalnum())

s1 = Solution()
print(s1.isPalindrome(str))
print(s1.isPalindrome_v2("1   7,9  7,1"))
# print(s1.isPalindrome_v2("17951"))
