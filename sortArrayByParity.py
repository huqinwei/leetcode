class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # ret = []
        # B = []
        # for i in A:
        #     # print('i:',i)
        #     if i % 2 != 0:
        #         B.append(i)
        #         # print('A',A)
        #     else:
        #         ret.append(i)
        # for j in B:
        #     ret.append(j)
        # return ret

        # 双指针，只需O(n)
        # l = 0
        # r = len(A) - 1
        # while l < r:
        #     if A[l] % 2 == 0:
        #         l += 1
        #         continue
        #     if A[r] % 2 == 1:
        #         r -= 1
        #         continue
        #
        #     A[l],A[r] = A[r],A[l]
        #     l += 1
        #     r -= 1
        # return A


        # 利用了整块复制，内建的加法，从O(n) + O(n)伴随循环赋值换成了一步赋值，O(n)
        odd=[]
        even=[]
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even+odd

a = [3,1,2,4,23,3,3,4,5,3,3,5,3,3,2,1,32,23]
# a.remove(3)
# print(a)
# a.append(2)
# print(a)

s1 = Solution()
ret = s1.sortArrayByParity(a)
print(ret)