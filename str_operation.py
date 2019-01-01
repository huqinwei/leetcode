str1 = 'strcpy'
str2 = str1
print(str1,str2)
print(id(str1),id(str2))
str1 = 'strcpy2'
print(str2)




str3 = ',hello,world,world,broke,away,away,home,'
print(str3)
print(str3.strip(','))
print(str3.lstrip(','))
print(str3.rstrip(','))
# print(str3)


str1 = 'strcat'
str2 = 'append'
str1 += str2
print(str1)

str1 = 'strchr'
str2 = 's'
nPos = str1.index(str2)
print(nPos)
nPos = str1.index('ch')
print(nPos)


import operator
str1 = 'strchr'
str2 = 'strchr'
# print(cmp(str1,str2))
print(operator.eq(str1,str2))

str1 = '12345678'
str2 = '456'
print(str1 and str2)
print(len(str1 and str2))

str1 = 'JCstrlwr'
print(str1)
str1 = str1.swapcase()
print(str1)
str1 = str1.upper()
print(str1)
str1 = str1.lower()
print(str1)
str1 = str1.capitalize()
print(str1)


str1 = '12345'
str2 = 'abcdef'
n = 3
str1 += str2[0:n]
print(str1)

str1 = '12345'
str2 = '123bc'
n = 4
print(operator.eq(str1[0:n],str2[0:n]))

str1 = ''
str2 = '12345'
n = 3
str1 = str2[0:n]
print(str1)

str1 = '12345'
ch = 'r'
n = 3
str1 = n*ch + str1[3:]
print(str1)















