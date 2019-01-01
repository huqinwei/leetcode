

class Solution:
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     j = 0
    #     i = 0
    #     total_c = 0
    #     while i < m+n:
    #         print('start with i:',i,' j:',j)
    #         c = 0
    #         tmp = []
    #         print('nums1:',nums1)
    #         print('nums2:',nums2)
    #         while j < n and nums2[j] < nums1[i]:
    #             tmp.append(nums2[j])
    #             j += 1
    #             c += 1
    #         print('c:',c)
    #         if c != 0:
    #             # print('i:',i)
    #             # print('c:',c)
    #             # print('m:',m)
    #             # print('before:',nums1)
    #             # nums1[i+c:i+m+c] = nums1[i:i+m]
    #             nums1[i+c:m+n] = nums1[i:i+m-total_c]#
    #             # print('before:',nums1)
    #             nums1[i: i + c] = tmp[:]
    #             # print('after:',nums1)
    #             i += c
    #             total_c += c
    #         # print('total_c:',total_c)
    #         # print('m:',m)
    #         if nums1[i] == 0:
    #             # print('i:',i)
    #             nums1[i] = nums2[j]
    #             j+=1
    #             # print('nums1:',nums1)
    #         if j >= n:
    #             break
    #
    #         i += 1
    #         # print('new i:',i)
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     i = 0
    #     j = 0
    #     total_c = 0
    #     while i < m + total_c:
    #         print('i:',i,' j:',j)
    #         print('nums1:',nums1)
    #         if nums2[j] < nums1[i]:
    #             nums1[i+1:i+m+1] = nums1[i:i+m]
    #             nums1[i] = nums2[j]
    #             # print(nums1)
    #             j += 1
    #             total_c += 1
    #         else:
    #             nums1[i+1] = nums2[j]
    #             j += 1
    #             total_c += 1
    #
    #         i += 1
    #         if j >= n:
    #             break
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     """
    #     # sort()可以换成手动快速排序。这个问题绕弯路的根本原因是，把数组的复制复杂化.
    #     # 数组不像链表，不需要刻意一段一段的拆解，数组可以整段移动。
    #     # 其实我前边的做法也用到了整段移动，所以，吃亏了。
    #     nums1[m:m+n] = nums2[:]
    #     print(nums1)
    #     nums1.sort()
    #     print(nums1)
    def merge(self, nums1, m, nums2, n):
        # 利用数组1后边的空间
        # two points
        p1 = m - 1
        p2 = n - 1
        p3 = m + n - 1
        # print('init:\tp1:{0}\tp2:{1}\tp3:{2}'.format(p1,p2,p3))

        while p3 >= 0:

            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p3] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[p3] = nums2[p2]
                    p2 -= 1
            elif p1 >= 0:
                nums1[p3] = nums1[p1]
                p1 -= 1
            elif p2 >= 0:
                nums1[p3] = nums2[p2]
                p2 -= 1


            p3 -= 1
            # print(nums1)
            # if p1 == -1 and p2 == -1:
            #     break
            # print('p1:{0}\tp2:{1}\tp3:{2}'.format(p1,p2,p3))


array = [1,2,3,0,0,0]
array2 = [2,5,6]

print(array)
# array[3:6] = array[0:3]
# print(array)
# array[0:3] = array2[:]
#
# print(array)


# array = [-1, -1]
# print(array)
# # print(array.index(2))
# # print(array.index(3))
# print(array.count(3))
# array2 = []
# # array2.sort()
# k = 2
# # a = array[:k]
# # print('a:',a)
# # a.sort()
# # print('a:',a)

s1 = Solution()
print('ret:',s1.merge(array,3,array2,3))#m=4,n=3
# print(s1.removeDuplicates(array2))
print(array)




