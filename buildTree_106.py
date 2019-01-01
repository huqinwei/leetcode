#   从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# 例如，给出
#
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 没有重复元素！
# 思路：从后序list拿[-1]，作为根，然后去中序list找这个value，把中序list分割成左右两部分向下迭代。
# 后序列表呢，把之前的[-1]拿掉以后也迭代下去，但是这里要按照中序list的左右来分割后序list为两部分。
# 之后其实就重复了！
# 关于树的具体构造过程，return的是treeNode，可以return之后从外部接起来
class Solution:
    def buildTree_failed(self, inorder, postorder):
        if not postorder:
            return None
        print('inorder:',inorder)
        print('postorder:',postorder)

        root_val = postorder[-1]
        print('root_val:',root_val)
        root = TreeNode(root_val)
        inorder_root_index = inorder.index(root_val)
        # 遇到问题，[2, 3, 1]和[3, 2, 1]，1是根，不能简单通过中序就觉得3是边缘，就在后序中拿3划分，把2就划给了右子树。
        # 所以不可避免的，应该把中序数组的根左边所有值都找出来？然后分别在后序数组中找到对应，最后一起拿走？别无他法？
        if inorder_root_index > 0:
            postorder_left_child_index = postorder.index(inorder[inorder_root_index-1])
            root.left = self.buildTree(inorder[:inorder_root_index],postorder[:postorder_left_child_index+1])

        if inorder_root_index < len(inorder) - 1:
            postorder_right_child_index = postorder.index(inorder[inorder_root_index+1])
            root.right = self.buildTree(inorder[inorder_root_index+1:],postorder[postorder_right_child_index:-1])

        return root

    # 我多余去用中序的根的左右分别去找后序了，因为中序根左右不一定是子树根，所以反倒失败了

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        node_center_frompost=postorder.pop()
        index_center_inorder=inorder.index(node_center_frompost)
        node=TreeNode(node_center_frompost)
        # 他的意思是，中序的根，左边有几个，后序的就是从前边拿几个！！！！
        node.left=self.buildTree(inorder[:index_center_inorder],postorder[:index_center_inorder])
        # 中序的根，右边的，后序当然也都是几个，不过后序的起点特殊，不像中序需要跳过一个根，所以没有 + 1，
        node.right=self.buildTree(inorder[index_center_inorder+1:],postorder[index_center_inorder:])#pop操作直接拿掉了[-1]，不用管了。
        return node


inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
inorder = [2,3,1]
postorder = [3,2,1]
s = Solution()
s.buildTree(inorder,postorder)



