#   路径总和
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
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
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


# maxdepth变形，把sum传下去就好了

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum_v1(self, root, sum):
        if not root:
            return False
        def dfs(root,local_sum):#问题应该在递归上，空子树就别让递归
            # print('depth:',depth)
            if root == None:
                print('none')
                # max_depth = depth
                print('local sum:',local_sum)
                print('sum:',sum)
                return local_sum == sum#叶节点判定有误，根1，左2，结果根到右边其实不算sum，但是我给算成了sum 1
            local_sum += root.val
            return dfs(root.left,local_sum) or dfs(root.right,local_sum)
        return dfs(root,0)

    # 第一版的叶子认定有问题，这是改进版
    def hasPathSum_myself(self, root, sum):
        if not root:
            return False
        def dfs(root,local_sum):
            local_sum += root.val
            if root.left == None and root.right == None:
                return local_sum == sum
            ret1 = ret2 = False
            if root.left:
                ret1 = dfs(root.left, local_sum)
            if root.right:
                ret2 = dfs(root.right, local_sum)
            return ret1 or ret2
        return dfs(root,0)

    def hasPathSum(self, root, sum):#他这个是整个函数的自我递归，把sum给递减了。
        if not root:
            return False
        elif not root.left and not root.right:
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(1)
p4 = TreeNode(9)
p1.left = p2
# p1.right = p3
# p3.left = p4
head = p1

s = Solution()
print(s.hasPathSum(head,1))

