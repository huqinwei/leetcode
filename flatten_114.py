
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

p1 = TreeNode(1)
p2 = TreeNode(2)
p5 = TreeNode(5)
p1.left = p2
p1.right = p5

p3 = TreeNode(3)
p4 = TreeNode(4)
p2.left = p3
p2.right = p4

p6 = TreeNode(6)
p5.right = p6





root = p1

class Solution:
    def flatten_fail(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root or (root.left == None and root.right == None):
            # print('return root')
            if not root:
                # print('none')
                pass
            else:
                # print('root.val:',root.val)
                # print('root.left:',root.left)
                # print('root.right:',root.right)
                pass
            return root
        # print('call,root is ',root.val)
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        root.left = None
        if left:
            # print('root is ',root.val)
            # print('left is ',left.val)
            root.right = left
            while left.right:
                left = left.right
            left.right = right
            # print('right is ',right.val)
        else:
            # root.right = right
            pass
        return root#这有一点问题，如果我想直接给flatten做递归，还想用return做衔接，其实他不让return东西

    def flatten_myself(self, root):#执行用时: 56 ms, 在Flatten Binary Tree to Linked List的Python3提交中击败了97.46% 的用户
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root or (root.left == None and root.right == None):
                # print('return root')
                if not root:
                    # print('none')
                    pass
                else:
                    # print('return    root.val:',root.val)
                    # print('root.left:',root.left)
                    # print('root.right:',root.right)
                    pass
                return root
            # print('do not return      root is ',root.val)
            left = dfs(root.left)
            right = dfs(root.right)
            root.left = None
            if left:
                # print('root is ',root.val)
                # print('left is ',left.val)
                root.right = left
                # print('current left:',left.val)
                while left.right:
                    # print('loop:current left:',left.val)
                    left = left.right
                left.right = right
                # print('right is ',right.val)
                # print('left.right is ',left.right.val)
            else:
                # root.right = right
                # print('do not have left ')
                pass

            # # 这种打印不能乱写，不然直接改了root了!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # root_to_print = root
            # while (root_to_print):
            #     print('__tree:', root_to_print.val)
            #     root_to_print = root_to_print.right


            return root
        dfs(root)


#视频讲的有个蠢方法，是用vector，不满足题意.前序遍历扔进vector，让vector的节点往后指


sol = Solution()
ret = sol.flatten(root)
print('ret:',ret)
while(root.right):
    print('val:',root.val)
    root = root.right