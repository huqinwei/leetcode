#   每个节点的右向指针
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
# 你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。
# 示例:
#
# 给定完美二叉树，
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# 调用你的函数后，该完美二叉树变为：
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL

import collections
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
# 思路：递归可能有点麻烦，要跨很多层去向右连接，还不如直接逐层访问，用deque，可能stack更好，把每一层连起来
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect_failed(self, root):
        if not root:
            return None
        stack = [root]
        while stack:
            next_point = None
            n = len(stack)
            for _ in range(n):
                cur = stack.pop()#只为了连接操作方便，忘了需要deque的特性，被破坏了
                cur.next = next_point
                next_point = cur
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
    def connect_myself(self, root):
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

    # 他这个方法是双指针的逐层遍历，题目假设每一层都是满的，所以他确实可以这么做，充分利用了这个特性让hptr去操作。然后用ptr.left去换层
    def connect(self, root):
        if not root:
            return
        ptr = root
        while ptr:
            hptr = ptr
            while hptr:
                hptr.left.next = hptr.right
                if hptr.next:
                    hptr.right.next = hptr.next.left
                hptr = hptr.next#从上向下，每一层已经给next连好了，所以hptr可以使用next遍历

            hptr = hptr.left







