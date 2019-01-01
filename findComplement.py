import numpy as np
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # sum = 0
        # while num:
        #     print("num:",num)
        #     print("num % 2:",num % 2)
        #     sum += (1 - (num % 2))
        #     num = num // 2
        #     print("after  num:",num)
        #     if num:
        #         sum *= 2
        # return sum
        # 全拼到一起做有点乱，不好截止
        ###########################################################
        #AC!!!!
        l = []
        sum = 0
        while num:

            # print(num,num % 2,1-num % 2)
            l.append(1 - num % 2)
            # print('l:',l)

            num = num // 2
        n = len(l)
        # print('n:',n)

        for i in range(n):
            # print(i,l[i])
            # print('(n -1 - i):',(n -1 - i))
            # sum += (2 ** (n -1 - i)) * l[i]
            sum += (2 ** (i)) * l[i]
            # print('sum:',sum)
        return sum
        ###############################################################################3



        ###############################################3
        # num = np.int32(num)
        # complement = np.int32(2**31 - 1)
        # print("%x"%complement)
        # print("%x"%num)
        #
        # com1 = complement ^ num
        # print("%x"%com1)
        # com2 = com1 & complement
        # print("%x"%com2)
        # return com2
    ######################################


s = Solution()
print('ret:',s.findComplement(9))

# print(3^2)
# print(2**31 - 1)







