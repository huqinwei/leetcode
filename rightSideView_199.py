# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
# 示例:
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p1.left = p2
p1.right = p3

p5 = TreeNode(5)
p4 = TreeNode(4)
p2.right = p5
p3.right = p4




#我觉得就是用queue来BFS，每次把整层都拿出来，然后给最后一个放进result

import collections
class Solution:
    def rightSideView_myself(self, root):#56 ms, 在Binary Tree Right Side View的Python3提交中击败了70.63% 的用户
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        queue = collections.deque()
        queue.append(root)

        while queue:
            n = len(queue)
            print('size:',n)
            for i in range(n):
                node = queue.popleft()
                if i == n - 1:
                    result.append(node.val)
                print('node:',node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        print('result:',result)
        return result



    def rightSideView(self, root):#视频讲的方法是用pair，每次压入数据的时候，配上它的层，这样读取的时候就是动态刷新每层最后一个点
        #56 ms, 在Binary Tree Right Side View的Python3提交中击败了70.63% 的用户
        # 执行用时: 52 ms, 在Binary Tree Right Side View的Python3提交中击败了87.50% 的用户

        result = []
        if not root:
            return result
        queue = collections.deque()
        queue.append((root,0))

        while queue:
            n = len(queue)
            print('size:',n)
            for i in range(n):
                node_tuple = queue.popleft()#强行区分这个tuple太费脑子，不如赋值给node和index更直观，大不了做完了再优化精简
                if node_tuple[1] >= len(result):#append
                    result.append(node_tuple[1])
                result[node_tuple[1]] = node_tuple[0].val#update
                print('node:',node_tuple[0].val)
                if node_tuple[0].left:
                    queue.append((node_tuple[0].left,node_tuple[1]+1))
                if node_tuple[0].right:
                    queue.append((node_tuple[0].right,node_tuple[1]+1))

        print('result:',result)
        return result


sol = Solution()
sol.rightSideView(p1)