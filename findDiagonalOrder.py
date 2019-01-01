# 给定一个含有
# M
# x
# N
# 个元素的矩阵（M
# 行，N
# 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
#
#
#
# 示例:
#
# 输入:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# 输出: [1, 2, 4, 7, 5, 3, 6, 8, 9]
#
# 解释:
#
# 说明:
#
# 给定矩阵中的元素总数不会超过
# 100000 。

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        if m == 0:
            return ret
        n = len(matrix[0])
        i = j = 0
        up_order = True
        while i < m and j < n:
            if up_order:
                ret.append(matrix[i][j])
                if j == n - 1:
                    i += 1
                    up_order = False
                    continue
                else:
                    j += 1
                if i == 0:
                    up_order = False
                    continue
                else:
                    i -= 1
            else:
                ret.append(matrix[i][j])
                if i == m - 1:
                    j += 1
                    up_order = True
                    continue
                else:
                    i += 1
                if j == 0:
                    # i += 1
                    up_order = True
                    continue
                else:
                    j -= 1

        return ret


l = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
l = []
s = Solution()
print('ret:',s.findDiagonalOrder(l))

