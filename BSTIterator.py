#   二叉搜索树迭代器
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 调用 next() 将返回二叉搜索树中的下一个最小的数。
# 注意: next() 和hasNext() 操作的时间复杂度是O(1)，并使用 O(h) 内存，其中 h 是树的高度。


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator_myself(object):#奇葩的定义。AC是AC了，不过空间复杂度没有降低到O(h)，是O(n）
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.data = []
        self.cur = -1
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.data.append(root.val)
            dfs(root.right)

        dfs(root)
        print(self.data)
        # return self.cur

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur < len(self.data) - 1:
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        self.cur += 1
        return self.data[self.cur]

class BSTIterator_v1(object):#这个思路是左子树压到底，往回弹,碰到右子树就新开递归
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = []
        self.putLeftTree(root)#把左侧一排都压栈了


    def putLeftTree(self, node):
        if node == None:
            return []
        else:
            while(node != None):
                self.tree.append(node)
                node = node.left

    def hasNext(self):
        return len(self.tree) > 0
    def next(self):
        node = self.tree.pop()#弹栈
        if node.right != None:
            self.putLeftTree(node.right)#如果有右节点，还压栈，当前的点仍然要返回
        return node.val#如果这个点没有有右节点，返回他自己

class BSTIterator(object):#这个和前一个例子一样，只不过是没封装的版本
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return self.stack

    def next(self):
        node = self.stack.pop()
        result = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return result

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

# Your BSTIterator will be called like this:
i, v = BSTIterator(root), []

while i.hasNext():
    v.append(i.next())
    print(v)
