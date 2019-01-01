#
# 473. 火柴拼正方形
#
# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
#
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。


# 注意:
# 给定的火柴长度和在 0 到 10^9之间。
# 火柴数组的长度不超过15。



# 火柴棍摆正方形。是深度优先搜索，带回溯。估计得用四个容器装一下4个边。
# 做一些优化剪枝。
# 求和，每条边不能大于1/4的sum。
# 排序，从大到小，1、1、2、2、3、3、4。如果是1,1，后边做再多尝试都是错的，如果是4，就不用尝试了，3，尝试到1就行了
# 如果不是出题，而是纯随机数，那么先看总和是否能被4整除，这能除去75%的情况









# 具体实现上，四个容器存下标，然后下标对应去查询排序后的数组
# 按下标的不同分配方便遍历深搜
# 而且占用的下标要用mark标出来，或者用in vec1 in vec2 in vec3来判断是否已经占用
# 从前向后，从大到小，跳过占用，逐个尝试，碰到剪枝条件返回。
# 回溯的话， 怎么恢复到之前状态？
# 所以说，四个容器只是让你判断边是否符合条件的，真正走遍历的，你还得有一个路径容器，因为是深度搜索加回溯，那就返回的时候删了新加的就行

#同样过程，C++就可以过
# class Solution {
# public:
#     bool
#
#
# makesquare(vector < int > & nums) {
# if (nums.size() < 4)
# return false;
# int
# sum = 0;
# for (int i = 0;i < nums.size();i++)
# sum += nums[i];
# if (sum % 4)
#     return false;
# std::sort(nums.rbegin(), nums.rend());
# int
# bucket[4] = {0};
# return generate(0, nums, sum / 4, bucket);
# }
# bool
# generate(int
# i, std::vector < int > & nums, int
# target, int
# bucket[])
# {
# if (i >= nums.size())
#     return target == bucket[0] & & target == bucket[1] & & target == bucket[2] & & target == bucket[3];
# for (int j = 0; j < 4; j++)
#     {
#     if (bucket[j] + nums[i] > target)
# continue;
# bucket[j] += nums[i];
# if (generate(i + 1, nums, target, bucket))
#     return true;
# bucket[j] -= nums[i];
#
# }
# return false;
# }
# };
import time
#实际看他的C++代码，也不用特别的路径保存之类的，i就正常遍历，那些个需要跳过的情况都通过遍历中的return回溯掉了，能走到最后的，当然就让他走到最后。中途回溯的方法，也就是加了多少就减去多少。。

# python能过，python3超时
class Solution:
    def generate(self,i,nums,target,bucket):
        # print(nums)
        # print(target)
        # print('bucket:',bucket)
        if i >= len(nums):
            if bucket[0] == target and bucket[1] == target and bucket[2] == target and bucket[3] == target:##与此同时，还用考虑i是否有多余吗？
                return True
            return False#但是如果i超了，肯定不能再继续了

        for j in range(4):
            if bucket[j] + nums[i] > target:#他判断的是加nums[i]之后的，小于和等于化为一类，因为是提前加，等于肯定还是要到后边执行。
                #但是这种提前加的方法，不是跳过了当前容器了？一个容器是3，+2超过4，跳过，但是3也没够啊！！所以不是逐个容器填满，而是逐个容器放元素，也可能每个容器都得再拿出来。究竟哪种快？不好说
                continue

            bucket[j] += nums[i]
            if self.generate(i+1,nums,target,bucket):
                return True
            bucket[j] -= nums[i]

        return False
    def makesquare(self, nums):#总之，这个题用python提交，就是超时！！！！！！！！！！！！！！！！！！！
        """
        :type nums: List[int]
        :rtype: bool
        """
        perimeter = sum(nums)
        if perimeter % 4 != 0 or perimeter == 0:
            return False
        nums.sort(reverse=True)
        print(nums)
        side = perimeter // 4
        bucket = 4*[0]
        return self.generate(0,nums,side,bucket)



# 位运算：
# 前提：长度不超过15,15位就够了。
#一个前提，按位取出下标，还要满足求和等于四分之一，这是数字的前提，不是任意数字都可以拿来比。
# 每个位代表一个下标对应元素是否出现，一个数字代表一条边，两个数字与操作，如果是0，进行或操作，产生一个新集合，就是半个正方体。
# 把这半个正方体的集合拿出来，还是要求两个与运算为零的前提，如果或运算等于11111111（长度视实际长度而定）？他说只要与运算为零就是True了，因为每条边都满足条件，每半个正方体也满足条件，如果他们还不相交，就足够了。
#

#
# 这个位运算的方法，算分治？

class Solution:
    def makesquare(self, nums):  # 总之，这个题用python提交，就是超时！！！！！！！！！！！！！！！！！！！从leetcode的表现看，这个反而不如前边的解法！因为超时!C++他讲课也说没做特殊优化，所以慢，对比是49ms和100ms以内
        perimeter = sum(nums)
        if perimeter % 4 != 0 or perimeter == 0:
            return False
        side_length = perimeter // 4
        # print('side_length:',side_length)
        valid_sides = []
        valid_half = []
        n = len(nums)
        for i in range(2**n):
            # print('###########################',i)
            #把这个数字拆解成下标，找到对应元素求和
            side = 0

            #way 1
            k = 1
            iter = i
            while iter:
                # print('iter:',iter)
                # print('n - k:',n - k)
                # print('nums[n - k]:',nums[n - k])
                if iter % 2 == 1:
                    # print('plus')
                    side += nums[n - k]
                k += 1
                iter = iter // 2#i >> 1
            #way 2他这种表达和我的好像反向了，我的nums[0]应该在这个数字i的比较大的位置，他这种是越靠后的数对应的是比较大的幂,但是后边应该都一样,不影响
            # for j in range(n):
            #     if i&(1<<j):
            #         side += nums[j]


            if side == side_length:
                valid_sides.append(i)
            # print('valid:',valid_sides)

        for i in range(len(valid_sides)):
            for j in range(i+1,len(valid_sides)):
                if valid_sides[i] & valid_sides[j] == 0:
                    valid_half.append(valid_sides[i]|valid_sides[j])
        # print('valid_half:',valid_half)
        for i in range(len(valid_half)):
            for j in range(i+1,len(valid_half)):
                if valid_half[i] & valid_half[j] == 0:
                    return True
        return False




nums = [1,1,2,2,2]
# nums = []
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# nums = [12,8,12,16,20,24,28,32,36,40,44,48,52,56,60]
# nums = [8,1,5,2,6,6,5,8,7,7,1,9,3,2,2]
# nums = [7215807,6967211,5551998,6632092,2802439,821366,2465584,9415257,8663937,3976802,2850841,803069,2294462,8242205,9922998]
nums = [5,5,5,5,16,4,4,4,4,4,3,3,3,3,4]
nums = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
# 输出: true

sol = Solution()
print('ret:',sol.makesquare(nums))


#
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 示例 2:
#
# 输入: [3,3,3,3,4]
# 输出: false
#
# 解释: 不能用所有火柴拼成一个正方形。

















#测一下sorted的reverse参数，不过感觉本题sort和sorted都行
# test_sort = [4,23,41,23,13,12,3,5,34,25,2134]
# print(sorted(test_sort))
# print(sorted(test_sort,reverse=True))
# print(test_sort)


#len()本身并不是瓶颈，不需要提前计算一下总长
# import time
# nums = 1000000*[0]
# start = time.time()
# length = len(nums)
# end = time.time()
# print(end-start)
# print(length)



a = 1
b = 2
print('a&b:',a&b)
print('a&b:',a|b)