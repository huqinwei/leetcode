# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1,length):
                print('i:',i,' j:',j)
                if nums[i] + nums[j] == target:
                    print(nums[i])
                    print(nums[j])
                    return [i,j]

    def twoSum_v2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if dict.get(complement) != None:
                return [dict.get(complement),i]
            dict[nums[i]] = i
            print(dict)

    def twoSum_v22(self, numbers, target):
        addDcit = {}
        for i in range(len(numbers)):
            if numbers[i] in addDcit and addDcit[numbers[i]] != i:
                return [addDcit[numbers[i]] + 1, i + 1]
            sub = target - numbers[i]
            addDcit[sub] = i


# 充分利用题给条件：有序
    def twoSum_v3(self, numbers, target):
        n = len(numbers)
        if n < 2:
            return []
        i = 0
        j = n - 1
        # print('numbers[i] + numbers[j]:',numbers[i] + numbers[j])
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1,j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1



#dict_demo
dict = {}
dict[4] = 500
dict[7] = 4
# print(dict.has_key(7))
print(dict.keys())
# print(dict.keys(500))
print(dict.get(4))
print(dict.get(2))
print(dict.items())
print('v:',dict.values())
print(dict)

print('dict:',dict)
print('500 in dict:',500 in dict)
print('4 in dict:',4 in dict)


#
# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement)) {
#             return new int[] { map.get(complement), i };
#         }
#         map.put(nums[i], i);
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }








s1 = Solution()
# print(s1.twoSum([3,2,4],6))
print(s1.twoSum_v3([1,2,4,5,7],6))