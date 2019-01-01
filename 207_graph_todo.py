#graph dfs demo
#做一个图的深度优先搜索


class GraphNode:
    def __init__(self,x):
        self.label = x
        self.neighbors = []

max_node = 5
Graph = [GraphNode(i)   for i in range(max_node)]
# print(Graph)
# print(Graph[0])
# print(Graph[0].label)
# print(Graph[1].label)

Graph[0].neighbors.append(Graph[4])#先插4，能测试回溯效果，先插2的话，4就被访问完了。
Graph[0].neighbors.append(Graph[2])

Graph[2].neighbors.append(Graph[3])
Graph[4].neighbors.append(Graph[3])

Graph[3].neighbors.append(Graph[4])#cycle:3<-->4


Graph[1].neighbors.append(Graph[0])
Graph[1].neighbors.append(Graph[2])



#DFS
visit = max_node*[0]

def dfs_graph(node,visit):
    visit[node.label] = 1
    print(' ',node.label)#肯定是“先根”的，注意，不能放到循环后

    for i in range(len(node.neighbors)):
        if visit[node.neighbors[i].label] == 0:
            dfs_graph(node.neighbors[i],visit)

for i in range(max_node):
    if visit[i] == 0:
        print('from label ',Graph[i].label)
        dfs_graph(Graph[i],visit)




#BFS
import collections
queue = collections.deque()

visit = max_node*[0]
#和树不同的点，不可能放一个“根”进去就完了，图可以有多“根”
for i in range(max_node):
    if visit[i] == 0:
        queue.append(Graph[i])
        # 暂时不用加size和for循环的，试一次原始的
        while(queue):
            # print('current queue',queue)
            node = queue.popleft()
            print('node:',node.label)
            visit[node.label] = 1
            for i in range(len(node.neighbors)):#不过这个for循环还是必要的，这是图的neighbors结构使然，其实等价于书的left和right的if语句
                #按照传统的树形访问，还会与到一个问题，重复：同一层，2的下一个是3,4的下一个也是3，所以必须判断queue中有什么，
                # 还必须同层判断吧？应该是必须的?比如2和4的下面不是3，而是2和4互联，4出去了，访问2,2的next还是4,4又压入了，虽然通过visit也能解决这个问题。看起来不把握?可能问题不大!
                if visit[node.neighbors[i].label] == 0 and node.neighbors[i] not in queue:
                    queue.append(node.neighbors[i])

print()
print()
#纠结的点主要还在于同时存在一个for循环de不可能只有“同一层”，如果用那种for size方法，就简单多了
queue = collections.deque()
visit = max_node*[0]

for i in range(max_node):
    if visit[i] == 0:
        queue.append(Graph[i])
        # 暂时不用加size和for循环的，试一次原始的
        while(queue):
            # print('current queue',queue)
            for i in range(len(queue)):
                node = queue.popleft()
                print('node:',node.label)
                visit[node.label] = 1
                for i in range(len(node.neighbors)):
                    if visit[node.neighbors[i].label] == 0 and node.neighbors[i] not in queue:
                        queue.append(node.neighbors[i])
# 也是因为有了visit辅助，如果没有visit辅助，这些逻辑怎么都不对，因为图够深啊，你当前一层不重复访问，下一层下下层不能保证
#或者两边层深就不一样，比如1->4->5->3，1->2->3
#反正大概就两种情况，同时在queue中，不同时在queue中，不同时在queue中，visit会先记录访问完的，同时在queue中，直接not in判断
#我生君未生，君生我已死。




print('*****************other*********************************')
#网课的方式，他是进队列就给标记了visit
queue = collections.deque()

visit = max_node*[0]
for i in range(max_node):
    if visit[i] == 0:
        queue.append(Graph[i])
        while(queue):
            node = queue.popleft()
            print('node:',node.label)
            visit[node.label] = 1
            for i in range(len(node.neighbors)):
                if visit[node.neighbors[i].label] == 0:
                    queue.append(node.neighbors[i])
                    visit[node.neighbors[i].label] = 1#他是进队列就给标记了visit


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

# 是我不理解题意？感觉用图的遍历不太好。考察的应该不是从一个点出发能否遍历所有点，肯定得有多个起点，独立课程肯定有吧？能否遍历完和是否有环不是一个概念， 2, [[1,0],[0,1]]也能遍历完
#
# 只是有环无环的话感觉还不如直接用链表！
#
# 或者是这网课给的思路不好，不容易联想到,他给的是反向画图，从被依赖的课程做出发点
#确实是要判断是否有环，但是单纯用访问过来判断也是不对的，2->1->0,2->0，这个过程都会访问0，但是这不叫环，这也是可以完成的
#所以是记录起点，然后逐个对比吗？
#好像不用考虑什么遍历周全不周全，就是某一个顶点，是否逐渐下一步能搜到它自己，只要能搜到它自己，就算有环，就算失败，这题不需要遍历节点，也许根本也不给全你节点？

numCourses = 5
prerequisites = [[4,0],[2,0],[3,2],[3,4],[4,3],[0,1],[2,1]]



# 
# 207. 课程表

# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 示例 2:
#
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
