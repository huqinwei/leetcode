#   旋转数组
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释:
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 说明:
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的原地算法。


class Solution:
    def rotate_slow(self, nums, k):
        # 提取最后一个作为tmp，按顺序后移，这个方法的局限性是只能移动1位，移动多了就冲突了，没处缓存，所以必须有技巧。传染式移动就必须找规律做限制
        # 这种比较死板的移动方法乘以k次，就算移动k次了
        # 但是超时了！！！！！！
        for _ in range(k):
            if len(nums) == []:
                return
            tmp = nums[-1]
            for i in range(len(nums) - 1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = tmp


    # 想用接力式方法，k!=n是肯定的，k和n的奇偶性应该也不同，n=4，k=2的话，一直原地踏步。如果满足了这个条件，是否n次就能遍历整个数组？
    # 但是，奇偶性相同的话，不代表就不移动了。输入: [-1,-100,3,99] 和 k = 2，输出: [3,99,-1,-100]
    # 奇偶性相同也是能动的，比如n=5，k=3，其实可以传递
    # 看做循环队列，想能顺利遍历所有元素，应该是k和n没有公约数，有的话就自然会重复
    # 有公约数用那个方法就不行了，但是也不能不处理啊，还得想办法处理！！
    # k = 4, n = 6, i = 0, i = 4, i = 8 % 6 = 2, i = 6 % 6 = 0，循环了。
    # 换个起点：i=1,i=5,i=3,但是规律是什么
    # 如果我用visited，肯定又犯法了.只能强行数学规律
    # 既然一次跳k，那我迭代不同的起点i，做k次循环，不分析公因数什么的，肯定就解决问题了，虽然可能存在冗余。
    # 如果不做无限循环，每次循环都是有限的，那么也就不容易有重复了吧，之前觉得有重复是因为一个循环有可能遍历所有。
    # 但是循环太短也不行啊，你不传递下去，那个多出来的值放哪？
    def rotate_todo(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return

    # 近乎作弊的参考答案：换成C + +怎么办？数组还能拆来拆去的？这应该就等于用了O(n - k)的空间复杂度吧？
    def rotate_cheat(self,nums,k):
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]

    # 基本都是作弊的，这个更是一不做二不休，extend又del
    def rotate_cheat2(self, nums, k):
        length=len(nums)
        k=k%length
        nums.extend(nums[:length-k])
        del nums[0:length-k]

    # 标准答案，是用技巧达到了前两个答案的移动效果
    def rotate(self, nums, k):
        def reverses(l,start,end):
            while(start<end):
                tmp=l[start]
                l[start]=l[end]
                l[end]=tmp
                start+=1
                end-=1
        if nums:
            k=k%len(nums)
            reverses(nums,0,len(nums)-1)# 第一步：整体翻转，数据逆序。
            reverses(nums,0,k-1)# 第二步：前k个局部翻转，就等于让数据恢复了本该有的正序。
            reverses(nums,k,len(nums)-1)# 第三步：后n - k个数据局部翻转，也是恢复本该有的正序。
            # 技巧在于选择多少个来翻转。，你选择多少个来翻转，就等于从后边切下来移到前边去多少个

s = Solution()
l = [1,2,3,4,5,6,7]
s.rotate_slow(l,3)
print(l)


a = [1,2,3]
print(a)
a.extend([4,5,6])
print(a)