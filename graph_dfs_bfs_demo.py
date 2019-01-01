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


