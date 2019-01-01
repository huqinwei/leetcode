#  验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 示例 1:
#
# 输入:
#     2
#    / \
#   1   3
# 输出: true
# 示例 2:
#
# 输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。

# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     root_list = []
    #     root_list.append(root.val)
    #     print('root_list:',root_list)
    #     return self.dfs(root,root_list)
    # def dfs(self,root,root_list):
    #     print('root_list:',root_list)
    #     if root.left:
    #         for v in root_list:
    #             print('root.left.val is :',root.left.val)
    #             print('v is :',v)
    #             if root.left.val >= v:#这样比还是不对，6在右子树15左下方，是该比15小，但是不应该比15的根10小，因为15是10的右子树
    #                 return False
    #         root_list2 = root_list.copy()
    #         root_list2.append(root.left.val)
    #         if self.dfs(root.left,root_list2) != True:
    #             return False
    #     if root.right:
    #         for v in root_list:
    #             print('root.right.val is :',root.right.val)
    #             print('v is :',v)
    #             if root.right.val <= v:
    #                 return False
    #         root_list3 = root_list.copy()
    #         root_list3.append(root.right.val)
    #         if self.dfs(root.right,root_list3) != True:
    #             return False
    #     return True
        # 左子树只包含大于当前节点的数，也就是说，需要跨层比较的，5的右子树根是15，15的左子树根是10，当前没问题，往上一层看，有问题。

        # 我需要一个结构把根的值层层传递下来，copy后的list？因为每一层都要保证，所以单传一个参数是不行的。
        # 你得记着左右关系？太乱了？
        # 实在不行，就别取巧了，简单粗暴点，把根的值传下去，遍历左子树，只要不合规定，就return false。然后遍历右子树。
        # 然后再往下取点，再这样遍历？肯定不对啊，这得遍历多少遍？！！！
        # 哦不对，既然是有顺序的树，我按顺序提取出来存进list，然后看看list是否有序。
    # 中序遍历
    def isValidBST_myself(self, root):

        if not root:
            return True
        val_list = []

        def dfs(root,val_list):
            if root.left:
                dfs(root.left,val_list)
            val_list.append(root.val)
            if root.right:
                dfs(root.right,val_list)

        dfs(root,val_list)
        #不能用sorted对比，有等于是不允许的
        if len(val_list) == 1:
            return True
        for i in range(1,len(val_list)):
            if val_list[i-1] >= val_list[i]:
                return False
        return True

    # 验证顺序而已，不需要专门存个list，只需要直接对比
    def isValidBST(self, root):
        if not root:
            return True
        self.last_value = -2**32

        def dfs(root):#这个全局的数，传参肯定是不对的？但是之前list也是这样做的，那是引用，不一样。
            if root.left:
                ret = dfs(root.left)
                if not ret:
                    return ret
            if root.val <= self.last_value:
                print('false')
                return False#递归如何return？这直接就被淹没了,只能自己处理吧，层层处理return
            print('last_value:',self.last_value)
            print('root.val:',root.val)
            self.last_value = root.val
            print('after:self.last_value:')
            if root.right:
                ret = dfs(root.right)
                if not ret:
                    return ret
            return True
        return dfs(root)

    ########################################################################################
    ########################################################################################
    # 为什么一定要是float（‘inf’）呢
    # 为了方便写递归函数，毕竟MIN也可能是root，MAX也可能是root
    # min和max的关键作用，是把爷爷的限制也传了下来，相当于在二叉树的图上画几条竖线
    # 如果一直朝右走，因为前边的都判断过了，所以子树只需要比根大，比2 ** 31小。
    # 如果出现左右转向：根的右子树的左子树，那么就是判断区间。
    # 从上到下，上边的数值已经没问题了，所以你不需要一直跑到大根部
    def isValidBST_uuuu(self,root):#copy
        def isvalid(root,min,max):
            print('root:{0},min:{1},max{2}'.format(root,min,max))
            if root == None:
                return True
            if root.val >= max or root.val <= min:
                return False
            return isvalid(root.left,min,root.val) and isvalid(root.right,root.val,max)#  and == &
            #逻辑真的很简单，每次迭代子树，带着根的值下去，另一方向（max或者min）直接传递。
        return isvalid(root,-2**32,2**32)#-float('inf'),float('inf')

    # 这个其实有一点二分查找和双指针的意思
    # root自身不用判断，参数也要传递，不能迭代最外层，自定义函数，起点是root的左右子树

    ###############################################
    ##########################################################################################
    #72ms下边这个答案持保留意见，感觉他对rootfirst和rootlast的理解都有问题
    def isValidBST_v2(self, root):
        """
        解法注意点：1.使用回溯法求解树的问题要时刻注意回溯问题的基例；而此题的Basecase为root==None
        2.BST节点左子树的最大节点值小于该节点，右子树最小节点值大于该节点。
        """

        def rootfirst(root):
            while root.left:
                root = root.left
            return root.val

        def rootlast(root):
            while root.right:
                root = root.right
            return root.val

        if not root:
            return True
        else:
            return (not root.left or rootlast(root.left) < root.val) and (
                        not root.right or rootfirst(root.right) > root.val) \
                   and self.isValidBST(root.left) and self.isValidBST(root.right)


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
print(s.isValidBST(head2))











