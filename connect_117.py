#  每个节点的右向指针 II
# 给定一个二叉树
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 说明:
#
# 你只能使用额外常数空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 示例:
#
# 给定二叉树，
#
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# 调用你的函数后，该二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL

# 不饱和的二叉树，用deque方案即可。

import collections
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        dq = collections.deque()
        dq.append(root)
        while dq:
            pre = None
            n = len(dq)
            for _ in range(n):
                cur = dq.popleft()#只为了连接操作方便，忘了需要deque的特性，被破坏了
                if pre:
                    pre.next = cur
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
                pre = cur
