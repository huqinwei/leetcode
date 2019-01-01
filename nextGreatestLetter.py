# 寻找比目标字母大的最小字母
# 给定一个只包含小写字母的有序数组letters 和一个目标字母 target，寻找有序数组里面比目标字母大的最小字母。
# 数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 并且有序数组为 letters = ['a', 'b']，则答案返回 'a'。
#

# 先和尾巴比较，超了就直接选第一个！
class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters:
            return ''
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        # left = 0
        # right = len(letters)
        # while left < right:
        #     mid = (left+right)//2
        #     print(left,right,' mid:',mid)
        #     if target >= letters[mid]:
        #         left = mid + 1
        #     elif target < letters[mid]:
        #         print('change right')
        #         right = mid
        # return letters[right]

        # 其他人的方法，前边一致
        ma = len(letters) - 1
        mi = 0

        while mi != (ma - 1):
            if letters[(ma + mi) // 2] <= target:
                mi = (ma + mi) // 2
            else:
                ma = (ma + mi) // 2

        return letters[ma]


# 示例:
#
# 输入:
letters = ["c", "f", "j"]
target = "a"


letters = ["c", "f", "j"]
target = "k"
target = "j"


# 输入:
letters = ["c", "f", "j"]
target = "d"
# 输出: "f"

#好像软件的题，找的是第一个超过某值的。
letters = ["e","e","e","e","e","e","n","n","n","n"]
target = "e"
#"n"

# 输入:
letters = ["c", "f", "j"]
target = "c"
# 输出: "f"

s = Solution()
print('ret:',s.nextGreatestLetter(letters,target))

# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "d"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "g"
# 输出: "j"


#
# letters长度范围在[2, 10000]区间内。
# letters 仅由小写字母组成，最少包含两个不同的字母。
# 目标字母target 是一个小写字母。