#   二叉树的前序遍历
# 给定一个二叉树，返回它的 前序 遍历。
#
#  示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,2,3]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal_myself(self, root):
        ret = []
        def dfs(root):
            if root:
                ret.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ret

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        p = root
        if p != None :
            ret.append(p.val)
        else:
            return ret
        if p.left != None:
            ret.extend(self.preorderTraversal(p.left))#看他的写法，这个list是可以迭代进去的，大概是因为return的也是list吧。
        if p.right != None:
            ret.extend(self.preorderTraversal(p.right))
        return ret


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right

s = Solution()
s.preorderTraversal(root)

#list.extend()    test!!!!!!!!!!!!!!!
list1 = [1,2]
list2 = [3,4]
list1.extend(list2)
print(list1)

