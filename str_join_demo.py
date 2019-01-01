#   只出现一次的数字
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,1]
# 输出: 1
# 示例 2:
#
# 输入: [4,1,2,1,2]
# 输出: 4
import collections
class Solution:
    # def singleNumber_too_slow(self, nums):
    #     c = []
    #     for i in nums:
    #         if i in c:
    #             c.remove(i)
    #         else:
    #             c.append(i)
    #         # print(c)
    #     return c[0]
    def singleNumber_slow(self, nums):
        c = collections.Counter()
        for i in nums:
            if i in c:
                del(c[i])
            else:
                c[i] += 1
            # print(c)
        return c.most_common()[-1][0]

    # 异或操作，没问题吗？负数怎么办？
    # 乍一看可能逻辑很不完善，1和2会被3消掉，但是基于题目条件，所有数组都成双成对，只有一个光棍，所以好像没有问题。
    def singleNumber_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in nums:
            result = result ^ i
            print(result)
        return result

    def singleNumber(self, nums):
        set1=list(set(nums))
        sum1=sum(set1)
        sum2=sum(nums)
        # print('nums:',nums)
        # print('set1:{0},sum1:{1},sum2:{2}'.format(set1,sum1,sum2))
        return 2*sum1-sum2

        # 也是利用了这个重复性，set1是去重的，那么set1的和乘以2减去nums的和，就是多出来的那一个！


s = Solution()
print(s.singleNumber([1,-12,3,1,3,-12,5]))


bstr=lambda x,l:''.join(('1' if x&(1<<i) else '0' for i in range(l,-1,-1)))
bstr.__doc__="""
给出数值的二进制格式化字符串
第一个参数被格式化数值
第二个参数最大位数
"""
print('test:',1 ^ 2)
print('test:',bstr(1^2,16))
print('test:',bstr(-3,16))


l = 32
x = 5
res = ''
for i in range(l,-1,-1):
    if x & (1<<i):
        res = res + '1'
    else:
        res = res + '0'
print('res:',res)
res2=''
res2 = res2.join('abc')
print('res2:',res2)
res2 = res2.join('eee')
print('res2:',res2)



a = ['H', 'e', 'llo']
b=''.join(a)
print(b)#'Hello'
c='-'.join(a)
print(c)#'H-e-llo'
d='*'
e=d.join(a)
print(e)#'H*e*llo'

# join不是简单的拼接'+'，是“join”，是用主语作为衔接把list拼起来，所以''.join('abc')不能理解为''.join('a') ''.join('b') ''.join('c')
list=['1','2','3','4','5']
print(''.join(list))
print(' '.join(['1','2','3','4','5']))

