
# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 返回:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

p1 = TreeNode(5)
p2 = TreeNode(4)
p3 = TreeNode(8)

p4 = TreeNode(11)

p6 = TreeNode(13)
p7 = TreeNode(4)


p4l = TreeNode(7)
p4r = TreeNode(2)
p7l = TreeNode(5)
p7r = TreeNode(1)


p1.left = p2
p1.right = p3

p2.left = p4
p3.left = p6
p3.right = p7

p4.left = p4l
p4.right = p4r

p7.left = p7l
p7.right = p7r


root = p1


sum = 22

class Solution:
    def pathSum_myself_v1(self, root, sum):
        if not root:
            return []

        result = []

        def dfs(root,sub_list,s):
            if root.left == None and root.right == None:
                if s == sum:
                    result.append(sub_list)
                return
            if root.left:
                dfs(root.left,sub_list+[root.left.val],s+root.left.val)
            if root.right:
                dfs(root.right,sub_list+[root.right.val],s+root.right.val)

        dfs(root,[root.val],root.val)
        return result

    def pathSum(self, root, sum):##优化：打算去除list复制，用stack实现,但是用stack的话你s要重新算还是会慢，如果不重新算，s这里出栈还要减去,也不用减，传的时候才加。
        ## 实测AC超过98%
        if not root:
            return []

        result = []
        stack = []

        def dfs(root,stack,s):
            if root.left == None and root.right == None:
                if s == sum:
                    result.append(stack.copy())##这，一定得复制，单纯append，还是会改变的
                return
            if root.left:
                stack.append(root.left.val)
                dfs(root.left,stack,s+root.left.val)
                stack.pop()
            if root.right:
                stack.append(root.right.val)
                dfs(root.right,stack,s+root.right.val)
                stack.pop()
        stack.append(root.val)
        dfs(root,stack,root.val)
        return result


sol = Solution()
print('ret:',sol.pathSum(root,sum))