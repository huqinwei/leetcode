#   对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isSymmetric_failed(self, root):#这个方法错在不分具体结构根1，左子树2，2左子树3.根1，右子树3，左子树2，最后是32123，其实他们不对称
    #     if not root:
    #         return True
    #     val_list = []
    #
    #     def dfs(root, val_list):
    #         if root.left:
    #             dfs(root.left, val_list)
    #         val_list.append(root.val)
    #         if root.right:
    #             dfs(root.right, val_list)
    #
    #     dfs(root, val_list)
    #     if len(val_list) == 1:
    #         return True
    #
    #     val_list_reverse = val_list.copy()
    #     print(val_list)
    #     val_list_reverse.reverse()
    #     print(val_list_reverse)
    #
    #     return val_list_reverse == val_list

    def isSymmetric_myself(self, root):
        if not root:
            return True

        def dfs(root1,root2):
            # print('root1:{0},root2:{1}'.format(root1.val,root2.val))
            if root1 == root2:#root1(point) == root2(point) == None
                return True
            elif root1 == None or root2 == None:#1 None
                return False
            if root1.val != root2.val:
                return False
            print('root1',root1.val,' root2',root2.val)
            return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)

        return dfs(root.left, root.right)




root = TreeNode(2)
pl = TreeNode(3)
pr = TreeNode(3)
pll = TreeNode(4)
plr = TreeNode(5)
prl = TreeNode(5)

root.left = pl
root.right = pr
pl.left = pll
pl.right = plr
pr.left = prl


head2 = TreeNode(1)
p21 = TreeNode(1)
head2.left = p21

s = Solution()
print(s.isSymmetric(root))


# print(True)
# print(False)
# print(True and False)
# print(True or False)




