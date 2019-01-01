from collections import deque

class Solution:
    def openLock_slow(self, deadends, target):
        # 这个方案逻辑通了，但是效率不行！
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        init = ['0','0','0','0']
        target = list(target)
        dead = []
        for i in deadends:#这块太繁琐了，但是只能先这么变换
            dead.append(list(i))
        # init = 0
        if target == init:
            return 0
        if init in dead:
            return -1

        dq = deque([init])
        visited = {}
        visited[str(init)] = 0
        while dq:
            pop = dq.popleft()
            # 困难点：返回最小转动次数，因为是BFS，deque里边不能很好反应深度,比如，第一层有A，第二层有BCDE，那么在大循环计数的话B和D就不相等了，其实应该是相等的
            # 所以先做了一个返回True的版本
            # 现在的方案还有一个问题：如果用visited排斥，少出现很多种路径，会不会影响计算最低访问?虽然按理说BFS先visited的不可能更深
            # 如果这样呢，从dq取出来，先看看自己的次数，再存就次数 + 1，这个次数用visited存,dict
            if pop == target:
                return visited[str(pop)]
            for i in range(len(target)):
                # up
                tmp = pop.copy()#copy也低效，但是不copy也不知道用哪种形式
                tmp[i] = (str)(((int)(tmp[i]) + 1) % 10)
                if tmp not in dead and str(tmp) not in visited:
                    dq.append(tmp)
                    visited[str(tmp)] = visited[str(pop)] + 1
                # down
                tmp = pop.copy()
                tmp[i] = (str)(((int)(tmp[i]) - 1) % 10)
                if tmp not in dead and str(tmp) not in visited:
                    dq.append(tmp)
                    visited[str(tmp)] = visited[str(pop)] + 1
        return -1
##########################################################################################
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # print('s')
        deadset = set(deadends)#访问过就不能访问，和deadend其实是一回事，所以被合并了
        if (target in deadset) or ("0000" in deadset): return -1
        que = deque()
        que.append("0000")
        visited = set(["0000"])
        step = 0
        while que:
            step += 1
            size = len(que)
            for i in range(size):#他是通过按size做for循环来稳定step的
                point = que.popleft()
                for j in range(4):#四个位，这个循环一样
                    for k in range(-1, 2, 2):#-1到2，跨度2，实现了-1和1的循环
                        # print('point:',point)
                        newPoint = [i for i in point]#这是紧凑字符串转化为常规list的方法
                        # print('newPoint:',newPoint)
                        newPoint[j] = chr((ord(newPoint[j]) - ord('0') + k + 10) % 10 + ord('0'))#用ascii编码的差进行数学计算
                        newPoint = "".join(newPoint)#空字符串.join数组，就是“紧凑”字符串，和str出来的不一样
                        if newPoint == target:
                            return step
                        if (newPoint in deadset) or (newPoint in visited):
                            continue
                        que.append(newPoint)
                        visited.add(newPoint)
        return -1



s = Solution()
print(s.openLock(["5555"],'2222'))


#注意这个字符串和数组的互转过程
point = '3322'
print(point)
newPoint = [i for i in point]
print(newPoint)
newPoint = "".join(newPoint)
print(newPoint)



# visited = {}
# init = ['0', '0', '0', '0']
# visited[str(init)]=4
# init = ['0', '0', '0', '3']
# visited[str(init)]=4
# print(type(visited))
# print((visited))
