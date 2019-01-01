#   旋转图像
# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 示例 1:
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]



# 要求原地转化，我的思路是先行列互换，后左右翻转。因为是n*n，所以行列互换应该没什么问题。
# 另外，相比遍历所有的点，因为是互换，感觉遍历一半就够了。既然是互换，遍历重复了反而会变回原样。
# 让j小于i就可以了，对角线不用动


class Solution:
    def rotate_myself(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for j in range(n//2):
            for i in range(n):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]

    # 最快的一个案例和我算法一样，但是可能系统有变化吧。
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    # 其他一些利用了API
    # def rotate(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: void Do not return anything, modify matrix in-place instead.
    #     """
    #     matrix[::] = zip(*matrix[::-1])
    #
    # def rotate(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: void Do not return anything, modify matrix in-place instead.
    #     """
    #     for i in range(len(matrix)):
    #         for j in range(i):
    #             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    #     for i in range(len(matrix)):
    #         matrix[i].reverse()

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

s = Solution()
s.rotate(matrix)
print(matrix)





