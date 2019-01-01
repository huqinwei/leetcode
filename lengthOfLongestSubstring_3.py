# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#

# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入:
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



# 思路：双指针，单指针回退法是不够用的，比如wepwkew，遇到第二个w的时候，回退一步，其实还是漏了e。
# 所以单指针回退，不如双指针滑动，遇到第二个w，本例left+1就解决了。
# 第一个简单的想法是，每次遇到重复，清空dict，left指针向右滑动一步，right也从left重新走，所有的都重新计算，其实这个虽然号称O(n)，其实是有重复的，可能是O(2n）吧。
# 最优的算法其实是，left逐渐右移，逐渐清除dict中对应的字符，直到w回到1个，也就是dict从wepw变成epw，满足条件，结束。left此时在e，right此时在w，总数还是3。既然追求效率，总数量肯定不能查dict了，手动+-吧。
# dict自身也可以手动做，做一个也许是128长的，他没说字符串内容包含数字和符号。

# 示例 1:
#
s = "abcabcbb"
s = "pwwkew"
s = 'dvdf'
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

class Solution(object):
    def lengthOfLongestSubstring_v1(self, s):#AC
        """
        :type s: str
        :rtype: int
        """
        result = current_result = 0
        dict = {}
        print(s)
        left = right = 0
        while right != len(s):
            print(dict)
            print(s[left:right])
            if dict.get(s[right],0) != 0:
                dict[s[left]] = 0#感觉这还能再优化，如果left刚好是right这个字符，移动一下left，right也直接入了，省一步
                left += 1
                current_result -= 1
                continue#do not add right

            dict[s[right]] = 1
            right += 1
            current_result+=1
            result = max(result,current_result)

        print(result)
        return result

    # 优化，如果left刚好是right这个字符，移动一下left，right也直接入了，省一步
    # 少停滞一步！但是优化一定注意代码结构，很容易乱。这是能调试，且有时间的情况下才能做的事，
    # 因为逻辑比之前又复杂了.因为本来就有continue这种操作了。要么就用另一种方法，在内部做个小循环，一直删到无重复。
    def lengthOfLongestSubstring(self, s):

        result = current_result = 0
        dict = {}
        print(s)
        left = right = 0
        while right != len(s):
            print(dict)
            print('current_result:', current_result)
            if dict.get(s[right],0) != 0:
                print('left:',left)
                print('right:',right)

                if s[left] == s[right] and left != right:
                    current_result -= 1
                    left += 1
                    # right -= 1#这个肯定不能有，优化的目的就是让这一步right不停滞，在这做个停滞就乱了
                    pass
                    #dict[s[left]] = 0##这一步有和没有一样，只做说明
                else:#不要随便合并if和else的公共操作，if不能走continue,合并也行，放前边???也不能乱放前边，if语句用了left，前边先改了left，肯定不行!!!!
                    dict[s[left]] = 0#感觉这还能再优化，如果left刚好是right这个字符，移动一下left，right也直接入了，省一步
                    current_result -= 1
                    left += 1
                    continue#do not add right

            dict[s[right]] = 1
            right += 1
            current_result+=1

            result = max(result,current_result)
            print('end of loop:',s[left:right])
            print('left:',left)
            print('right:',right)
            print(dict)

        print(result)
        return result



print(s[0]==s[3])


sol = Solution()
sol.lengthOfLongestSubstring(s)

















