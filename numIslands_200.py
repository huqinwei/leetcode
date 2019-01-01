from collections import deque
class Solution:

    def numIslands_dfs(self, grid):#dfs
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        column = len(grid[0])
        row = len(grid)
        cnt = 0
        # print('row:{0},column:{1}'.format(row,column))
        for i in range(row):
            for j in range(column):
                # print('i:{0},j:{1}'.format(i,j))
                if grid[i][j] == '1':
                    self.combine_v2(grid,j,i)
                    cnt += 1
        return cnt

    def combine(self,grid,x,y):#用方向数组来描述
        grid[y][x] = '2'
        dx = [-1,1,0,0]#4方向，x\y肯定有一个是0，不是8方向，别写错
        dy = [0,0,1,-1]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if (new_x >= 0 and new_x < len(grid[0])) and (new_y >= 0 and new_y < len(grid)) and grid[new_y][new_x] == '1':
                self.combine(grid,new_x,new_y)

    def combine_old(self,grid,x,y):
        # print(grid)
        # print('x:{0},y:{1}'.format(x,y))
        grid[y][x] = '2'#这里改了原数组，如果不想改数组，新建一个mark数组
        # print('after:',grid)

        if x > len(grid[0]) - 1 and y > len(grid) - 1:
            return
        #up[y-1][x]
        if y - 1 >= 0 and grid[y-1][x] == '1':
            self.combine_old(grid,x,y-1)
        #down[y+1][x]
        if y + 1 < len(grid) and grid[y+1][x] == '1':
            self.combine_old(grid,x,y+1)
        #left:[y][x-1]
        if x - 1 >= 0 and grid[y][x-1] == '1':
            self.combine_old(grid,x-1,y)
        #right:[y][x+1]
        if x + 1 < len(grid[0]) and grid[y][x+1] == '1':
            self.combine_old(grid,x+1,y)


###################################################################
    #下面是BFS方法
    #优化改程序要注意一些变量的冲突，比如容器dq和坐标数组dp、dq，还有方向循环for i和大循环for i、for j
######################################################################3
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        if grid == []:
            return 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if  grid[i][j] == '1':
                    count += 1
                    dq = deque([(i,j)])
                    while dq:
                        p,q = dq.popleft()
                        grid[p][q] = '0'
                        # 容易丢一步：not in dq，但是我提前让主体等于0了，BFS又不是DFS，主体的上下左右难道还会有重复？
                        # 本回合没有重复，下回合会有重复，本回合有右和下，下回合就有两个右下，重复了，更多回合就不堪设想。
                        #BFS方法不同于DFS，DFS是一个递归结束才走另一个，所以标记位肯定被处理了，BFS用了queue，有标记位v待处理还未处理的
                        #up:i-1,j
                        dx = [-1, 1, 0, 0]  # 4方向，x\y肯定有一个是0，不是8方向，别写错
                        dy = [0, 0, 1, -1]
                        for k in range(4):
                            new_p = p + dx[k]
                            new_q = q + dy[k]
                            if (new_p >= 0 and new_p < row) and (new_q >= 0 and new_q < column) and (grid[new_p][new_q] == '1') and (new_p,new_q) not in dq:
                                # self.combine(grid, new_x, new_y)
                                dq.append((new_p,new_q))

        return count

    # 这个可能更快一些:todo
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     def bfs(i, j):
    #         if i == -1 or j == -1 or i == x  or j == y:
    #             return 0
    #         if grid[i][j]=='1':
    #             grid[i][j] = '0'
    #             bfs(i + 1, j)
    #             bfs(i, j + 1)
    #             bfs(i - 1, j)
    #             bfs(i, j - 1)
    #     if grid==None:
    #         return 0
    #     if len(grid)==0:
    #         return 0
    #     x=len(grid)
    #     if len(grid[0])==0:
    #         return 0
    #     y=len(grid[0])
    #     island=0
    #     for i in range(x):
    #         for j in range(y):
    #             if grid[i][j]=='1':
    #                 island+=1
    #                 bfs(i,j)
    #     return island

input =[['1','1','0','0','0',],
        ['1','1','0','0','0',],
        ['0','0','1','0','0',],
        ['0','0','0','1','1',]]
s = Solution()
print('island number:',s.numIslands(input))

# s.test1(input)
print(input)



#test deque
# for i in range(3):
#     for j in range(2):
#         # dq = deque((i, j))# deque([2, 1, (4, 5)])
#         dq = deque([(i, j)])# deque([(2, 1), (4, 5)])
#         print(dq)
#         dq.append((4,5))
#         print(dq)
#         while dq:
#             p,q = dq.popleft()
#             print('p:{0},q:{1}'.format(p,q))












