
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
class Solution:
    def subsets_myself_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        sub_list = []
        def func(sub_list,nums):
            # print('sub_list:',sub_list)
            if not nums:
                result.append(sub_list)
                return
            new_sub_list = sub_list.copy()
            func(new_sub_list,nums[1:])
            new_sub_list2 = sub_list.copy()
            new_sub_list2.append(nums[0])
            func(new_sub_list2,nums[1:])

        func(sub_list.copy(),nums)
        print(result)
        return result
    def subsets_myself_v2(self, nums):#关于形参和真假拷贝，尝试优化
        result = []
        def func(sub_list,nums):
            print('nums:',nums)
            print('sub_list:',sub_list)
            if not nums:
                result.append(sub_list)
                return
            func(sub_list,nums[1:])
            func(sub_list + [nums[0]],nums[1:])

        func([],nums)
        # print(result)
        return result

    # 实测，nums[1:]这种传参方式算复制，感觉直接用index可能会更快!实际提交没什么差别，52ms和60ms来回跳，版本2也就52ms
    def subsets_myself_v3(self, nums):
        result = []
        n = len(nums)
        index = 0
        def func(sub_list,index):
            # print('nums:',nums)
            # print('sub_list:',sub_list)
            if index == n:
                result.append(sub_list)
                return
            func(sub_list,index+1)
            func(sub_list + [nums[index]],index+1)

        func([],index)
        # print(result)
        return result


nums = [1,2,3]
sol = Solution()
print('ret:',sol.subsets(nums))

'''
l1 = [1,2,3,4]
# print(l1[4:])

# l1 + 5#wrong
# l1 + [5]#wrong
l1 += [5]#正确的给链表直接加元素的方法
print('l1:',l1)

def func(l):
    l.append(199)
    print('func:',l)
def func2(l):
    l.append(333)
    print('func2:',l)


if True:
    if True:# 这个加操作等同于复制数值,可能意思是拿的表达式的右值
        func(l1 + [200])#func2: [1, 2, 3, 4, 5, 333]
    else:#compare
        func(l1)#func2: [1, 2, 3, 4, 5, 199, 333]
    func2(l1)
else:#append操作，作为表达式，是None值,进入函数内部，None.apend，失败
    if True:
        func(l1.append(200))#AttributeError: 'NoneType' object has no attribute 'append'
    else:
        func(l1)
    func2(l1)


print(l1)


l2 = [1,2,3]
print('ret:',l2.append(4))#none

l3 = l2 + [4]#这算复制
print(id(l2))#140259104243336
print('id l3:',id(l3))#140259126260552
print(l2)
print(l3)


#探索另一处优化，就是我每次传的部分nums是否算复制。。。能删元素应该不算复制数组???NO!!!!!!!!!!!!。
print('before:',l3)
def func3(nums):
    print('id:',id(nums))
    del nums[0]
func3(l3)
print('after:',l3)
func3(l3[1:])
print('after:',l3)##经过对照组，其他的确实是复制的，只有完整的传才不算复制
func3(l3[2:])
print('after:',l3)
func3(l3[3:])
print('after:',l3)
print(id(l3))
print(id(l3[:]))
print(id(l3[1:]))
print(id(l3[2:]))
'''