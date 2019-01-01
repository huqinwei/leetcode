# 二叉树的层次遍历
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def levelOrder_myself(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if root == None:
            return ret
        dq = collections.deque()
        dq.append(root)
        k = 0
        while(dq):
            ret.append([])
            for _ in range(len(dq)):
                pop = dq.popleft()
                ret[k].append(pop.val)
                if pop.left:
                    dq.append(pop.left)
                if pop.right:
                    dq.append(pop.right)
            k += 1
        return ret
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        result = []
        while q:
            nodes_value = []
            for i in range(len(q)):
                node = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                nodes_value.append(node.val)
                del q[0]
                print('q:',q)
            result.append(nodes_value)
            print('result:',result)
        return result

p1 = TreeNode(10)
p2 = TreeNode(5)
p3 = TreeNode(15)
p4 = TreeNode(6)
p5 = TreeNode(20)
p1.left = p2
p1.right = p3
p3.left = p4
p3.right=p5
head = p1

head2 = TreeNode(1)
p21 = TreeNode(1)
head2.left = p21

s = Solution()
print(s.levelOrder(head))