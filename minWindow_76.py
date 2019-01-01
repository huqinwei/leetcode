s = 'ADOBECODEBANC'
t = 'ABCDAB'
char_map_len = 128
map_s = [0] * char_map_len
map_t = [0] * char_map_len

for c in s:
    map_s[ord(c)] += 1

for c in t:
    map_t[ord(c)] += 1

print(map_s)
print(map_t)
cnt_t = []
for i in range(char_map_len):
    if map_t[i] > 0:
        cnt_t.append(i)
print(cnt_t)
for i in cnt_t:
    print(chr(i))


def is_window_ok(map_s,map_t,cnt_t):
    for i in cnt_t:
        if map_s[i] < map_t[i]:
            return False
    return True
print(is_window_ok(map_s,map_t,cnt_t))


# 给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。
#
# 示例：
#
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

class Solution:
    def is_window_ok(self,map_s, map_t, cnt_t):
        for i in cnt_t:
            if map_s[i] < map_t[i]:
                return False
        return True
    def minWindow(self, s, t):
        result = ''
        min_window_len = len(s)#init

        char_map_len = 128
        map_s_window = [0] * char_map_len
        map_t = [0] * char_map_len
        cnt_t = []
        for c in t:
            map_t[ord(c)] += 1
        for i in range(len(map_t)):
            if map_t[i]>0:
                cnt_t.append(i)

        left = right = 0
        n = len(s)
        while right !=n:
            map_s_window[ord(s[right])] += 1

            #每次新加一个字符进来，尝试移动left，删除多余字符
            while left != right:
                val = ord(s[left])

                # if (val not in cnt_t) or (map_s_window[val] > map_t[val]):#两种情况，这个字符压根不在t中，这个字符在t中，但是数量足够。
                #     map_s_window[val] -= 1
                #     left += 1
                # else:
                #     break
                #这个方法的not in太费时间了？尝试优化(根本上来说，这个cnt_t不是在这搜索用的，是is_window_ok用的)！！！   #可能是t常量级的，没有本质区别。
                if map_t[val] == 0:
                    left += 1
                elif map_s_window[val] > map_t[val]:
                    map_s_window[val] -= 1
                    left+=1
                else:
                    break


            if self.is_window_ok(map_s_window,map_t,cnt_t):
                #if right - left + 1 <= min_window_len:##要包含等于，因为至少要更新一次，s='a',t='a'
                if result == '' or right - left + 1 <= min_window_len:#这两种方法都能解决问题
                    min_window_len = right - left + 1
                    result = s[left:right+1]
            right += 1
        return result

S = "ADOBECODEBANC"
T = "ABC"
S = 'a'
T = 'a'

sol = Solution()
print('ret:',sol.minWindow(S,T))









