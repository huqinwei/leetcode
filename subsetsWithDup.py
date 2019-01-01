#1,2,2,和2,1,2本质确实还是不一样的，分不开，唯一的方法是先排序，这样就不会出现了
nums = [2,1,2,3]
s1 = set()
s1.add((1,2,3))
s1.add((1,2,2))
s1.add((1,2,2))
s1.add((2,1,2))
s1.add(tuple(nums[1:4]))
print('s1:',s1)


class Solution:
    def subsetsWithDup_myself(self, nums):
        nums.sort()
        result = []
        temp_result = set()

        def func(sub_list, nums):
            if not nums:
                temp_result.add(tuple(sub_list))
                return
            func(sub_list, nums[1:])
            func(sub_list + [nums[0]], nums[1:])

        func([], nums)
        for v in temp_result:
            result.append(list(v))
        return result

    def subsetsWithDup(self, nums):
        res = [[]]
        nums = sorted(nums)
        len_nums = len(nums)
        last_len = 0
        for num_id in range(len_nums):
            if num_id == 0 or nums[num_id] != nums[num_id-1]:
                last_len = len(res)
                res += [one + [nums[num_id]] for one in res]
            else:
                temp = len(res)
                res += [one + [nums[num_id]] for one in res[last_len:]]
                last_len = temp
        return res

    def subsetsWithDup(self, nums):
        result = [[]]
        nums.sort()
        temp_size = 0
        for i in range(len(nums)):
            if i >=1 and nums[i] ==nums[i-1]:
                start = temp_size
            else:
                start = 0
            temp_size = len(result)
            for j in range(start,temp_size):
                result.append(result[j]+[nums[i]])
        return result


sol = Solution()
ret = sol.subsetsWithDup(nums)
print(ret)
# result = []
# for i in ret:
#     print(i)
#     print([i])
#     print('list(i):',list(i))
#     # print('list[i]:',list[i])
#     result.append(list(i))
# print(result)
#
# result2 = list(ret)
# print('result2:',result2)










