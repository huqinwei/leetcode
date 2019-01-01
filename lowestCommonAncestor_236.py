#   二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 说明:
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。


# 纯递归方案的话，返回值要灵活变化，True、False、node三种，True和False就好好比较，node就直接向上返


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 纯递归方案的话，返回值要灵活变化，True、False、node三种，True和False就好好比较，node就直接向上返
    def lowestCommonAncestor_myself(self, root, p, q):
        if not root:
            return False
        ret0 = root == p or root == q

        ret1 = self.lowestCommonAncestor(root.left,p,q)
        ret2 = self.lowestCommonAncestor(root.right,p,q)
        if (ret1 and ret2) or (ret0 and ret1) or (ret0 and ret2) :
            return root
        return ret1 or ret2 or ret0

    # 这个方案根据题目限制条件高度定制化

    # 下边这个算法的核心思想就是一直遍历到底，找不到就是None，这个None层层返回，那么只要有return非None，就是一个点。
    def lowestCommonAncestor_(self, root, p, q):
        # 他这个方案总感觉不会成功，如果3在5的下面，碰到5就return了，3不是找不到了？其实不需要找了，5自身就是交叉点，除非3在其他子树，那就共同return
        # 如果这个值是下边的，那当然返上去对比了，如果这个值真的是交叉点，那就返回这个点了。总共就这两种情况
        if not root or root == p or root == q:#这一点是技巧点
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:#关于对比方式，他是用的返回node，如果两个node都存在，那就是root这个node了
            return root
        else:
            return left if left else right
    def lowestCommonAncestor_math(self, root, p, q):#这个直接利用了数学特性，都在左子树；都在右子树；以这个根为交点。p和q之一不存在的情况return None
        if root == None or p == None or q == None:
            return None
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

    #一个用栈的思路，找到根到p和根到q的路径，两个路径来对比，如果一致，就是公共祖先，一直往后找，找到最后一个公共祖先




    def lowestCommonAncestor(self, root, p, q):#C+++++++++++++++++++++实现的方法，传的全是指针和引用，还不太好写,
        final_result = root
        def __preorder(root, target, path):#其实使劲改改，还是能return回去list的，懒得弄了！！！！！！！！！！他的原逻辑就是不借助return的，用各种指针返回
            print('path:',path)
            if not root or self.finish:
                return;#这个逻辑很不python！！
            path.append(root)
            if root == target:  # 注意，这里只找一个点，不管那么多
                finish = True
                self.result = path#not global...#主要问题是这个东西传不出来，这个逻辑很不python！！
                print('result:',self.result)
            __preorder(root.left, target, path)
            __preorder(root.right, target, path)
            path.pop()

        self.finish = False
        self.result = []
        __preorder(root,p,[])
        print('after,result:',self.result)
        result_p = self.result.copy()

        self.finish = False
        self.result = []
        __preorder(root,q,[])
        print('after,result:',self.result)

        print('result_p:',result_p)
        print('result:',self.result)

        if len(result_p) < len(self.result):
            path_len = len(result_p)
        else:
            path_len = len(self.result)
        for i in range(path_len):
            if result_p[i] == self.result[i]:
                final_result = self.result[i]
        return final_result



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


s = Solution()
ret = s.lowestCommonAncestor(head,p1,p2)
if ret:
    print(ret.val)








