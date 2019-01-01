# /*
#  * Return true if there is a path from cur to target.
#  */
# boolean DFS(int root, int target) {
#     Set<Node> visited;
#     Stack<Node> s;
#     add root to s;
#     while (s is not empty) {
#         Node cur = the top element in s;
#         return true if cur is target;
#         for (Node next : the neighbors of cur) {
#             if (next is not in visited) {
#                 add next to s;
#                 add next to visited;
#             }
#         }
#         remove cur from s;
#     }
#     return false;
# }

# "该逻辑与递归解决方案完全相同。 但我们使用 while 循环和栈来模拟递归期间的系统调用栈。 手动运行几个示例肯定会帮助你更好地理解它。"
# java不熟，但是我觉得这不叫DFS，在你取出cur->next->next之前，所有的cur - next都入栈了，这是BFS
# 除非这个for循环有特别含义，应该没这个可能

# 给定一个二叉树，返回它的中序 遍历。
#
# 示例:
#
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？


# 看不懂这个输入，你函数接口是treenode，示例却是list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal_recur(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []

        self.inorder(root,ret)

        return ret

    def inorder(self,node,ret):
        if node.left:
            self.inorder(node.left,ret)
        ret.append(node.val)
        if node.right:
            self.inorder(node.right,ret)

    # 其他人的答案，压栈，先根后左，出栈就是先左后根，都出完，再压右，稍微比那个费脑
    # 压是一口气压到最左，出可是一次出一个，就等于在一个子树上，从左节点退回到根节点，再压入右节点
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        if root == None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        '''
        stack = []
        ans = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            s = stack.pop()
            ans.append(s.val)
            root = s.right
        return ans




t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.left = t3

s = Solution()
print(s.inorderTraversal(t1))








