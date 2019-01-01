#  Search in a Binary Search Tree
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。
#
# 例如，
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和值: 2
# 你应该返回如下子树:
#
#       2
#      / \
#     1   3
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right,val)
        elif val < root.val:
            return self.searchBST(root.left,val)



p1 = TreeNode(10)
p2 = TreeNode(5)
p3 = TreeNode(15)
p4 = TreeNode(11)
p5 = TreeNode(20)
p1.left = p2
p1.right = p3
p3.left = p4
p3.right=p5
root = p1

s = Solution()
node = s.searchBST(root,13)
if node:
    print(node.val)
else:
    print('none')


