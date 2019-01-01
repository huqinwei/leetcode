
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
root = TreeNode(8)
for node in nodes:
    print(node.val)
    BST_insert(root,node)
preorder_print(root,0)
print("################")
midorder_print(root,0)
print(BST_search(root,3))
print(BST_search(root,10))
print(BST_search(root,140))













