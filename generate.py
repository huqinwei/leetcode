#   杨辉三角
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate_myself(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(numRows):
            ret.append([])
            for j in range(i+1):
                if ret[i-1]:
                    if j > 0 and j < i:
                        ret[i].append(ret[i-1][j-1] + ret[i-1][j])
                    else:
                        ret[i].append(1)
                else:
                    ret[i].append(1)
        return ret

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list1 = []
        for i in range(numRows):
            if i in (0, 1):
                temp = [1] * (i + 1)
                list1.append(temp)
            else:
                temp = [1] * (i + 1)#提前分配的方法，提前做一个一维数组temp，改完后直接给list1去追加temp（先放进去也行，总之数量确定了）
                for j in range(1, i):#他是先分配好了，再去改指定下标
                    temp[j] = list1[i - 1][j] + list1[i - 1][j - 1]
                list1.append(temp)
        return list1


s = Solution()
print('ret:',s.generate(6))






