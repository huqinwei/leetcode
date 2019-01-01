# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 第 k 个最大的元素，而不是第 k 个不同的元素。
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        a = nums[:k]
        a.sort()
        print('a:',a)
        for i in range(k,len(nums)):
            print('i:',i)
            if nums[i] > a[0]:
                j = 1
                while j < k:
                    if nums[i] > a[j]:
                        a[j-1] = a[j]
                        j += 1
                    else:
                        break
                print('j:',j)
                a[j-1] = nums[i]
                print('a:',a)

        print('a:',a)
        return a[0]
    def findKthLargest_api(self, nums, k):
        return heapq.nlargest(k,nums)[-1]
    def findKthLargest(self, nums, k):
        l = []
        for i in range(len(nums)):
            if len(l) >= k:
                if nums[i] > l[0]:
                    heapq.heappop(l)
                    heapq.heappush(l,nums[i])
                    #heapq.heapreplace(l,-nums[i])
            else:
                heapq.heappush(l, nums[i])
        return l[0]
    def findKthSmallest(self, nums, k):
        l = []
        for i in range(len(nums)):
            if len(l) >= k:
                if -nums[i] > l[0]:
                    heapq.heappop(l)
                    heapq.heappush(l,-nums[i])
                    #heapq.heapreplace(l,-nums[i])
            else:
                heapq.heappush(l, -nums[i])
            print(l)
        return -l[0]

array = [1,32,23,553,23,55,23]
# array = [-1, -1]
print(array)
# print(array.index(2))
# print(array.index(3))
print(array.count(3))
array2 = []
# array2.sort()
k = 2
# a = array[:k]
# print('a:',a)
# a.sort()
# print('a:',a)

s1 = Solution()
# print('ret:',s1.findKthLargest(array,2))
print('ret:',s1.findKthSmallest(array,6))
# print(s1.removeDuplicates(array2))
print(array)



array = [1,32,23,553,23,55,23]
heapq.heapify(array)
heapq.heappush(array,100)
print(array)
heapq.heapreplace(array,3)
print(array)
