

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BST_insert(root,node):
    if node.val == root.val:
        return root
    if node.val < root.val:
        if root.left:
            BST_insert(root.left,node)
        else:
            root.left = node
    else:
        if root.right:
            BST_insert(root.right,node)
        else:
            root.right = node
def BST_search(root,val):
    if root.val == val:
        return True
    if val < root.val:
        if root.left:
            return BST_search(root.left,val)
        else:
            return False
    elif val > root.val:
        if root.right:
            return BST_search(root.right,val)
        else:
            return False


def preorder_print(root,layers):
    if not root:
        return
    for i in range(layers):
        print('-----',end=' ')
    print(root.val)
    preorder_print(root.left,layers+1)
    preorder_print(root.right,layers+1)
def midorder_print(root,layers):
    if not root:
        return
    midorder_print(root.left,layers+1)
    for i in range(layers):
        print('-----',end=' ')
    print(root.val)
    midorder_print(root.right,layers+1)


nums = [3,10,1,6,15]
nodes = []
for x in nums:
    nodes.append(TreeNode(x))


# root = TreeNode(8)
# for node in nodes:
#     print(node.val)
#     BST_insert(root,node)

##另一种写法,8也在nodes数组，直接把nodes[0]当root传入
nodes.insert(0,TreeNode(8))
print('nodes:',nodes)
for i in range(1,len(nodes)):
    BST_insert(nodes[0],nodes[i])
root = nodes[0]








preorder_print(root,0)
print("################")
midorder_print(root,0)
print(BST_search(root,3))
print(BST_search(root,10))
print(BST_search(root,140))


#谁是根重要吗？是我只要保证查找效果一样？还是必须保证节点位置也一样？可能需要结合前序和中序？
#其实他就是简单的的保证搜索性，没保证结构，关于根节点的构建也很简单，就是拿出第一个数据，而不用管那个BST_Insert函数的通用性。
#不是，他用的是先根法，先根法第一个确实是根
class Codec:
    def preorder_print(self,root):
        if not root:
            return
        self.nums.append(str(root.val))
        self.preorder_print(root.left)
        self.preorder_print(root.right)

    def BST_insert(self,root, node):
        if node.val == root.val:
            return root
        if node.val < root.val:
            if root.left:
                self.BST_insert(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                self.BST_insert(root.right, node)
            else:
                root.right = node
    def serialize(self, root):
        self.nums = []
        self.preorder_print(root)
        ret = '#'.join(self.nums)
        print('ret:',ret)
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        print('data:', data)
        # root = TreeNode(data[0])#这是不对的，大数怎么办，所以那个#必须用上
        # data = data.strip('#')
        data = data.split('#')
        root = TreeNode(int(data[0]))
        for x in data[1:]:
            node = TreeNode(int(x))
            self.BST_insert(root,node)
        # preorder_print(root,0)
        return root




c1 = Codec()
data = c1.serialize(root)
c1.deserialize(data)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))