#   螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        ret = []
        m = len(matrix)
        if m == 0:
            return ret
        n = len(matrix[0])
        direction = 1
        i = 0
        j = -1
        current_m = m - 1
        current_n = n
        current_step = 0
        # ret.append(matrix[i][j])
        while True:#not current_m or not current_n:
            # ret.append(matrix[i][j])
            # print('direction:',direction)
            # print('i:',i,' j:',j)
            if direction == 1:
                if current_step < current_n:
                    j += 1
                    ret.append(matrix[i][j])
                    current_step += 1
                else:
                    direction = 2
                    current_n -= 1
                    current_step = 0
            elif direction == 2:
                # print('current_step:',current_step,' current_m:',current_m)
                if current_step < current_m:
                    i += 1
                    ret.append(matrix[i][j])
                    current_step += 1
                else:
                    direction = 3
                    current_m -= 1
                    current_step = 0
            elif direction == 3:
                if current_step < current_n:
                    j -= 1
                    ret.append(matrix[i][j])
                    current_step += 1
                else:
                    direction = 4
                    current_n -= 1
                    current_step = 0
            elif direction == 4:
                if current_step < current_m:
                    i -= 1
                    ret.append(matrix[i][j])
                    current_step += 1
                else:
                    direction = 1
                    current_m -= 1
                    current_step = 0
            if direction % 2 == 1 and current_n == 0:#(direction == 1 or direction == 3)
                print('break1')
                break
            if direction % 2 == 0 and current_m == 0:
                print('break2')
                break


        return ret

l = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
l = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

s = Solution()
print('ret:',s.spiralOrder(l))
