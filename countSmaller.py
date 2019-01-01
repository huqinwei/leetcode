
class Solution:

    def merge_sort_two(self,nums1,nums2):
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j+=1
        for k in range(i,len(nums1)):
            result.append(nums1[k])
        for k in range(j,len(nums2)):
            result.append(nums2[k])
        return result

    def merge_sort(self,nums):
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2

        nums1 = self.merge_sort(nums[0:mid])
        nums2 = self.merge_sort(nums[mid:])

        return self.merge_sort_two(nums1,nums2)
    # 他假设这两个子序列有序。
    # 前提是，两边相等时，算法是优先插左边的。
    #
    # 归并排序过程中：
    # 他这个规律是，既然不逆序，左边的元素互相都不干扰，你count是几，说明右边有几个比你小的，所以在归并排序过程中，就是j对应的值，j = 0，说明一个比你小的都没有。
    # 所以解法就是，进行归并排序，然后在排序过程中，顺便给左边的就给存了count，然后归并能把右边的也分解成左右。
    #
    # 感觉这么个归并过程，count不只是j，是count += j，好几层累加呢。
    # 但是返回顺序怎么办，我返回的结果顺序要原来的，不是打乱后的，得做一个映射，但是最起码，理论上是可行的。
    # 所以就是做一个映射，一个dict或者pair这样的东西，我无论怎么排序，都给原始的那个count做累加，就得到结果了
    #
    # 那么重复的部分呢，如果你先插右边的，左边的count认定就会多 + 1，实际上5不是5的逆序数，不应该加，但是他也没保持不动，他合并了？没有！！！这个图还没完，你看1就是双份。
    # 明显感觉到，即便思路有了，实现也差点，数据结构和接口这些还是欠缺。我觉得如果是python，就用一个tuple就行了吧，tuple[0]
    # 存nums的实际值，tuple[1]
    # 存对应count中的下标，我只去比tuple[0]，然后找到count[tuple[1]]
    # 去做增量操作


    #我需要给排序那个做变形，我传进去的可能是[tuple()]
    def countSmaller(self, nums):#AC:364ms
        n = len(nums)
        count = n * [0]
        nums = [(i,nums[i]) for i in range(len(nums))]
        ret = self._merge_sort(nums,count)
        return count

    def _merge_sort_two(self,nums1,nums2,count):
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i][1] <= nums2[j][1]:
                result.append(nums1[i])
                count[nums1[i][0]] += j
                i += 1
            else:
                result.append(nums2[j])
                j+=1
        for k in range(i,len(nums1)):
            result.append(nums1[k])
            count[nums1[k][0]] += j
        for k in range(j,len(nums2)):
            result.append(nums2[k])
        return result

    def _merge_sort(self,nums,count):#分治过程不用改，主要去改排序实际操作，根据映射修改count就好了
        n = len(nums)
        if n < 2:
            return nums
        mid = n // 2
        nums1 = self._merge_sort(nums[0:mid],count)
        nums2 = self._merge_sort(nums[mid:],count)

        return self._merge_sort_two(nums1,nums2,count)

    # 第二个方法，逆置数组，由求后边比自己小的个数，改成求前边比自己小的个数，给节点加个计数器，每次比某一节点大，加上这个计数。
    # 当然，这个计数器维护也需要考虑
    #往它左子树插1，计数器+1，往它右子树插的话，当前节点不计，右子树的数量记在当前节点的父节点。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 0
        self.repeat = 0

class Solution2:
    def BST_insert(self,root, node,total_count):#因为是递归的，total count要传参进去
        print('##################current node:',node.val)
        if node.val == root.val:
            total_count += root.count

            #这也是个坑点，碰到重复元素，计数器还是要更新的，你一堆2,3来了不可能只算一个吧...但是加了好像也不对，比2小的是1，我再碰到2，却给2这个点+1，那以后碰到2，不是也加1了？
            #碰到重复的2时，其实我应该做的，是给2的右子树全都 + 1.。。。。
            #或者我再用一个计数器，就是计算重复的
            #都怪那个网课坑，他说用一个count，我不知道他想怎么利用一个count解决这个重复问题
            #他的方法是，重复的也插入，插前边
            root.repeat += 1
            return total_count
        if node.val < root.val:
            root.count += 1#update counter
            print('node',root.val,'\'scount updated to:',root.count)
            if root.left:
                return self.BST_insert(root.left, node,total_count)
            else:
                root.left = node
        else:
            print('node > root')
            total_count += root.count
            total_count += root.repeat
            total_count += 1#include root self
            if root.right:
                return self.BST_insert(root.right, node,total_count)
            else:
                root.right = node
        return total_count
    def countSmaller(self, nums):
        if not nums:
            return []
        nums = nums[::-1]
        n = len(nums)
        count = n * [0]
        print('reversed:',nums)
        root = TreeNode(nums[0])
        for i in range(1,len(nums)):
            print('nums[i]:',nums[i])
            node = TreeNode(nums[i])
            current_cnt = self.BST_insert(root,node,0)
            print('current count:',current_cnt)
            count[i] = current_cnt



        print('count:',count)
        count = count[::-1]
        print('count:',count)
        return count


class Solution3:
    def BST_insert(self, root, node, total_count):  # 因为是递归的，total count要传参进去
        if node.val <= root.val:
            root.count += 1  # update counter#其实在等于的时候，这样改，已经改坏了，但是之前已经拿到想要的结果了，所以不影响。
            if root.left:
                return self.BST_insert(root.left, node, total_count)
            else:
                root.left = node
        else:
            total_count += root.count
            total_count += root.repeat
            total_count += 1  # include root self
            if root.right:
                return self.BST_insert(root.right, node, total_count)
            else:
                root.right = node
        return total_count

    def countSmaller(self, nums):
        if not nums:
            return []
        nums = nums[::-1]
        n = len(nums)
        count = n * [0]
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            node = TreeNode(nums[i])
            current_cnt = self.BST_insert(root, node, 0)
            count[i] = current_cnt

        count = count[::-1]
        return count


nums1 = [1,6,9,13,22,55,222]
nums2 = [2,7,8,15,22,77,344]
sol = Solution()
print('ret:',sol.merge_sort_two(nums1,nums2))


nums = [3,3,4,5,5,2,3,34,3,42,324]
print('ret:',sol.merge_sort(nums))
nums = [3,2,2,3,1,2,0]
sol.countSmaller(nums)

print('hello')
sol2 = Solution3()
sol2.countSmaller(nums)









