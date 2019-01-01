# 将有序数组转换为二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST_myself(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if not n:
            return None
        mid_index = (n-1)//2
        # print('index:',mid_index)
        root = TreeNode(nums[mid_index])
        def dfs(root,l_index,r_index):
            # if l_index >
            mid = (r_index - l_index) // 2 + l_index#warning: + l_index is needed
            root.val = nums[mid]
            print('l:{0},mid:{2},r:{1},val:{3}'.format(l_index,r_index,mid,root.val))
            if l_index < mid:
                print('l loop')
                child = TreeNode(0)
                root.left = child
                dfs(child,l_index,mid)

            if mid < r_index-1:#主要问题在于处理左右一致性,左闭右开，右边那个值不用
                print('r loop')
                child = TreeNode(0)
                root.right = child
                dfs(child,mid+1,r_index)
            print('end')

        dfs(root,0,n)#主要问题在于处理左右一致性，统一不用右边的，所以第一步传的是n，不是n-1,。
        return root

    # 别人的很简洁，不知道这个传参法nums算不算复制，好像并不算。
    # 他用return root来牵线
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

l = [-10,-3,0,5,9]
s = Solution()
root = s.sortedArrayToBST(l)





