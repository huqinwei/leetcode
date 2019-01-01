class Solution:
    def findMinArrowShots_myself(self, points):##可能慢在了count=len(points)，白白多计算一次,实测时间差不多，可能就是leetcode网站的问题,for循环也需要知道len()，可能通过优化，两者相同

        points.sort()
        count = len(points)
        cur_min = cur_max = 0
        for i in range(len(points)):
            if cur_min >= cur_max:
                cur_min = points[i][0]
                cur_max = points[i][1]
            else:
                if points[i][0] <= cur_max:
                    count -= 1
                    cur_max = min(cur_max,points[i][1])
                else:
                    cur_min = points[i][0]
                    cur_max = points[i][1]
        return count
    def findMinArrowShots(self, points):##可能慢在了count=len(points)，白白多计算一次,实测时间差不多，可能就是leetcode网站的问题,for循环也需要知道len()，可能通过优化，两者相同
        points.sort()
        count = 0
        cur_min = cur_max = 0
        for i in range(len(points)):
            if cur_min >= cur_max:
                count += 1
                cur_min = points[i][0]
                cur_max = points[i][1]
            else:
                if points[i][0] <= cur_max:#因为排序过了，所以不更新min貌似也没关系，比的就是max
                    cur_max = min(cur_max,points[i][1])
                else:
                    count += 1
                    cur_min = points[i][0]
                    cur_max = points[i][1]
        return count



l1 = [[10,16], [2,8], [1,6], [7,12]]


sol = Solution()
print('ret:',sol.findMinArrowShots(l1))






l1 = [[10,16], [2,8], [6,6], [1,12]]



l2 = sorted(l1,key=(lambda x:x[0]))
l3 = sorted(l1,key=(lambda x:x[1]))


l1.sort()
print(l1)
print('l2:',l2)
print('l3:',l3)