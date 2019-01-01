#   二叉树的后序遍历
# 给定一个二叉树，返回它的 后序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal_myself(self, root):
        ret = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                ret.append(root.val)
        dfs(root)
        return ret
    def postorderTraversal(self,root):
        ret = []
        if root == None:
            return ret
        #left
        if root.left:
            ret.extend(self.postorderTraversal(root.left))
        if root.right:
            ret.extend(self.postorderTraversal(root.right))

        ret.append(root.val)
        return ret



root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right

s = Solution()
print('ret:',s.postorderTraversal(root))
