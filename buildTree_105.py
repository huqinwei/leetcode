#   从前序与中序遍历序列构造二叉树
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return
        # root_val = preorder.pop()
        root_val = preorder[0]
        preorder.remove(root_val)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        # print('index:',root_index)
        if root_index > 0:
            root.left = self.buildTree(preorder[:root_index],inorder[:root_index])
        if root_index < len(inorder) - 1:
            root.right = self.buildTree(preorder[root_index:],inorder[root_index+1:])
        return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s = Solution()
s.buildTree(preorder,inorder)