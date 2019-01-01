from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:#不一定等于1，可能被改成1234567，只要不是0，都需要遍历
                    dq = deque([(i,j)])
                    # dq.append((i,j))
                    # print((i,j) in dq)
                    # print(dq)
                    step = 0
                    visited = []
                    visited.append((i,j))
                    finded = False
                    while dq:
                        if finded:
                            break
                        size = len(dq)
                        # print('dq:',dq,' while i,j is ',i,j)
                        for _ in range(size):
                            point = dq.popleft()
                            # print('point:',point)
                            if matrix[point[0]][point[1]] == 0:
                                matrix[i][j] = step
                                # print('                     matrix:',matrix)
                                finded = True#双层循环的break问题,看来在while里边加一个for循环来计算step是有弊端的，用一个标记来解决
                                break
                            # up\down\left\right
                            if point[0] < len(matrix) - 1 and (point[0]+1,point[1]) not in dq and (point[0]+1,point[1]) not in visited:
                                dq.append((point[0]+1,point[1]))
                                visited.append((point[0]+1,point[1]))
                            if point[1] < len(matrix[0]) - 1 and (point[0],point[1]+1) not in dq and (point[0],point[1]+1) not in visited:
                                dq.append((point[0],point[1]+1))
                                visited.append((point[0],point[1]+1))
                            if point[0] > 0 and (point[0]-1,point[1]) not in dq and (point[0]-1,point[1]) not in visited:
                                # print('1:append:',point[0]-1,point[1])
                                dq.append((point[0]-1,point[1]))
                                visited.append((point[0]-1,point[1]))
                            # print(point[0],point[1])
                            if point[1] > 0 and (point[0],point[1]-1) not in dq and (point[0],point[1]-1) not in visited:
                                # print('2:append:',point[0],point[1]-1)
                                dq.append((point[0],point[1]-1))
                                visited.append((point[0],point[1]-1))

                        step += 1
        return matrix





image = [[0,0,0],[0,1,0],[1,1,1]]

s = Solution()
print(s.updateMatrix(image))