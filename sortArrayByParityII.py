class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """


        # 双指针，
        # l = 0
        # r = 1
        # n = len(A)
        # while l < n and r < n:
        #     print(l,r)
        #     if A[l] % 2 == l % 2:
        #         l += 2
        #         continue
        #     if A[r] % 2 == r % 2:
        #         r += 2
        #         continue
        #     # step如果是1，双指针的问题：我需要奇数，你需要奇数，我只有偶数，你只有偶数，饿死了
        #     # 如果step是2，左右双指针和全左快慢双指针应该是一样的
        #     # print('before swap:',A)
        #     A[l],A[r] = A[r],A[l]
        #     # print('after swap:',A)
        #     l += 2
        #     r += 2
        # return A
        # 没有多占用空间，但是不限制空间，所以亏了
        # 复杂度没差吧，可能亏在双重判定上了，if语句太多
        # 我觉得在整体都比较规整的情况下，可能更快？至少少了很多赋值操作，判定还是要有。如果很规整，大部分情况也只走一个if



        # 每个循环只有一个if,小优势
        res = [0] * (len(A))
        odd = 1
        even = 0
        for x in A:
            if x % 2 == 0:
                res[even] = x
                even += 2
            else:
                res[odd] = x
                odd = odd + 2
        return res


a = [2,3,1,1,4,0,0,4,3,3]
# a.remove(3)
# print(a)
# a.append(2)
# print(a)

s1 = Solution()
ret = s1.sortArrayByParityII(a)
print(ret)