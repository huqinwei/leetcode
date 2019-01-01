# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
#
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
#
# 示例 1:
#
# 输入:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 示例 2:
#
# 输入:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。


# 他这个是矩阵，是行列，横竖看：
# [[1,1,0],代表0和自己要“连着”，和1连着。
#  [1,1,0],代表1和自己要“连着”，和0连着。
#  [0,0,1]],代表2和自己要“连着”



#最直觉的方式是DFS，和岛屿一样
#可以直接套岛屿，一样的数据结构
#与岛屿的不同之处在于，可以旋转，因为这个数组传递的是关系。可以旋转的是x，y不行。
# 也不对，不是岛屿问题，第一个点可以直接和第三个点相连，数组上看，没有相邻。所以本质上不是一个靠相邻就能解决的问题。
class Solution:
    def DFS(self,M,visited,i):
        visited[i] = 1
        for j in range(len(M[0])):
            if M[i][j] and not visited[j]:
                self.DFS(M,visited,j)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        cnt = 0
        visited = [0  for i in range(len(M))]
        # print(visited)
        for i in range(len(M)):
            if M[i] and not visited[i]:
                # print('cnt++')
                cnt += 1
                self.DFS(M,visited,i)
                # print(visited)

        return cnt


nums = \
    [[1,1,0],
 [1,1,0],
 [0,0,1]]
nums = \
[[1,0,0,1],
 [0,1,1,0],
 [0,1,1,1],
 [1,0,1,1]]
sol = Solution()
print('ret:',sol.findCircleNum(nums))


# #并查集的本质就是重定向，本来都是独立的个体，通过无数个重定向，集中到一起。
# 但是这个操作有没有顺序影响？A指向B，B指向C，A还能指向C吗？
#
# 另外，这是数组实现，按理说可以dict或者set来实现。

class DisjointSet(object):
    def __init__(self,n):
        self.id = [i for i in range(n)]
        print(self.id)
    def find(self,p):
        return self.id[p]

    def union(self,p,q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return;
        for i in range(len(self.id)):#这里，不止一个，以前A指向B，现在A和B的值都是pid，所以A和B都指向qid。
            if self.id[i] == pid:
                self.id[i] = qid
        print('id is ',self.id)

#上边这是基本结构，但是要做这道题，要用变形才会快，因为你不能费力合并半天，还要费时间去两两比较。给加一个counter，合并了就减少counter,其实仍然不够快
#这样，把原题拿来构建并查集，最后的count就是结果
class DisjointSet(object):
    def __init__(self,n):
        self.id = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.count = n

    def find(self,p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]#其实路径压缩根本不用管位置，路径压缩确实就是跳一步，但是因为“终点”是自己指向自己，你跳也不怕跳出问题
            p = self.id[p]
        return p

    def union(self,p,q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return;
        if self.size[i] < self.size[j]:#保持平衡，i小，则i指向j
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count-=1

class Solution:
    def DFS(self,M,visited,i):
        visited[i] = 1
        for j in range(len(M[0])):
            if M[i][j] and not visited[j]:
                self.DFS(M,visited,j)

    def findCircleNum(self, M):
        d_set = DisjointSet(len(M))
        for i in range(len(M)):
            for j in range(i+1,len(M[0])):#小优化，这是双向关系，所以j不用遍历n，从i+1开始
                if M[i][j]:
                    d_set.union(i,j)

        return d_set.count



d = DisjointSet(7)
d.union(0,5)
print(d.id)
# print(d.find(0))
print(d.id)
print(d.size)
d.union(2,4)
print(d.id)
print(d.size)
d.union(0,4)
print(d.id)
print(d.size)

sol = Solution()
print('ret:',sol.findCircleNum(nums))



