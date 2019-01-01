#   Kth Largest Element in a Stream
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
#
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.cnt = 1
#用什么二叉搜索树失败，不知道为什么这个题归类到那了
class KthLargest_fail:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.root = 0
        if not nums:
            return
        print('assign self root')
        for i in range(0,len(nums)):
            ret = self.add(nums[i])
            print('ret:',ret)

    # 优化：如果插入完再寻找，过程会很慢，可以考虑两个过程掺杂在一起。
    # 但是插入的遍历和顺序遍历并不一样，插入是最大h，而查找第k大是n，我只能用计数器，按顺序逐个查找。
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        #insert
        if self.root == 0:
            self.root = TreeNode(val)
        else:
            print('insert val:',val)
            root = self.root
            while root:
                if val > root.val:
                    print('>')
                    if root.right:
                        root = root.right
                        continue
                    else:
                        print('create:',val)
                        root.right = TreeNode(val)
                        break
                elif val < root.val:
                    if root.left:
                        root = root.left
                        continue
                    else:
                        root.left = TreeNode(val)
                        break
                else:
                    root.cnt += 1
                    break

        #search k大应该是用右中左的顺序遍历
        root = self.root
        self.cnt = 0
        def r_m_l(root):
            if not root:
                return None
            print('access node:',root.val)


            ret = r_m_l(root.right)
            if ret:
                return ret

            cnt = root.cnt
            print('root:',root.val,' cnt:',cnt)
            while cnt:
                self.cnt += 1
                cnt -= 1
                if self.cnt == self.k:
                    return root.val

            ret = r_m_l(root.left)
            if ret:
                return ret

        return r_m_l(root)
import heapq
#最小堆，维护一个堆，k个数字，然后从堆中直接拿最后一个
class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        # print(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        if self.size < self.k:
            heapq.heappush(self.pool,val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool,val)
        return self.pool[0]

s = KthLargest(3,[4,5,8,2])
s = KthLargest(1,[])
print('add ret:',s.add(-3))
print('add ret:',s.add(-2))
print('add ret:',s.add(-4))
print('add ret:',s.add(0))
print('add ret:',s.add(4))

# 堆的定义：
# 堆是一种特殊的数据结构，它的通常的表示是它的根结点的值最大或者是最小。
# python中heapq的使用
# 列出一些常见的用法：
# heap = []#建立一个常见的堆
# heappush(heap,item)#往堆中插入一条新的值
# item = heappop(heap)#弹出最小的值
# item = heap[0]#查看堆中最小的值，不弹出
# heapify(x)#以线性时间将一个列表转为堆
# item = heapreplace(heap,item)#弹出一个最小的值，然后将item插入到堆当中。堆的整体的结构不会发生改变。
# heappoppush()#弹出最小的值，并且将新的值插入其中
# merge()#将多个堆进行合并
# nlargest(n , iterbale, key=None)从堆中找出做大的N个数，key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字
l = [1,5,8,6,2,3]
heapq.heapify(l)
print(type(l))#heapify以后，是个list
print(l)
print('pop:',heapq.heappop(l))
print(l)
print('push:',heapq.heappush(l,4))
print(l)
print('push:',heapq.heappush(l,0))
print(l)
size = len(l)
print('largest:',heapq.nlargest(3,l))
print('largest:',heapq.nlargest(5,l))
print('largest:',heapq.nlargest(15,l))



k = 3
while size > k:#heapify以后，虽然是个list，但是是个树形结构？[0]确实最小，后边的无序啊
    print('pop:',heapq.heappop(l))
    size -= 1
    print(l)
print('heap top is :',l[0])

#insert
size = len(l)
if size == k:
    heapq.heapreplace(l,20)
    print('after replace:',l)
# print('top:',l.top())
print('top:',l[0])
print(heapq.nlargest(53,l))
print(heapq.nlargest(3,l))
print(heapq.nlargest(2,l))


