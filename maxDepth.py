#   二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。


# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth_myself(self, root):#BFS
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        dq = collections.deque()
        dq.append(root)
        step = 0
        while dq:
            for _ in range(len(dq)):
                root = dq.popleft()
                if root.left:
                    dq.append(root.left)
                if root.right:
                    dq.append(root.right)
            step += 1
        # print('step:',step)
        return step

    def maxDepth(self, root):

        def dfs(root,depth):
            # print('depth:',depth)
            if root == None:
                # max_depth = depth
                return depth
            return max(dfs(root.left,depth + 1),dfs(root.right,depth + 1))

        return dfs(root,0)

    #DFS
    def maxDepth_other(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))#他省略了传参过程，是返回时+1




p1 = TreeNode(4)
p2 = TreeNode(5)
p3 = TreeNode(1)
p4 = TreeNode(9)
p1.left = p2
p1.right = p3
p3.left = p4
head = p1

s = Solution()
print(s.maxDepth(None))











