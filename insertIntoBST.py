#   Insert into a Binary Search Tree
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
#
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
#
# 例如,
#
# 给定二叉搜索树:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# 和 插入的值: 5
# 你可以返回这个二叉搜索树:
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# 或者这个树也是有效的:
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST_bak(self, root, val):#没说清楚题意，万一你要的就是当前节点呢，或者有变种题，就用这个
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif val > root.val:#right
            if root.right:
                return self.insertIntoBST(root.right,val)
            else:
                node = TreeNode(val)
                root.right = node
                return node
        elif val < root.val:
            if root.left:
                return self.insertIntoBST(root.left,val)
            else:
                node = TreeNode(val)
                root.left = node
                return node

    def insertIntoBST_myself(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val == val:
            return
        elif val > root.val:#right
            if root.right:
                self.insertIntoBST(root.right,val)
            else:
                node = TreeNode(val)
                root.right = node
        elif val < root.val:
            if root.left:
                self.insertIntoBST(root.left,val)
            else:
                node = TreeNode(val)
                root.left = node
        return root

    def insertIntoBST(self, root, val):#这是不递归调用的版本
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)
        temp = root
        while 1:
            if temp.val > val:
                if not temp.left:
                    temp.left = TreeNode(val)
                    break
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = TreeNode(val)
                    break
                else:
                    temp = temp.right
        return root
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
s.insertIntoBST(root,7)
print(p1.left.right.val)