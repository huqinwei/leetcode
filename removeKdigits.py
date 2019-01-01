# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。

# 示例 2 :
#

# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
# 示例 3 :
#
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。


class Solution:
    # 1396ms#能过，但是低效，冗余是肯定有的，每次从头遍历，但是不知道怎么取巧
    #主要是操作上的坑，想要del一个，我就得break，重新循环，不然最后会越界，本来可以不break，继续找下去的。
    def removeKdigits_myself(self, num, k):
        num = list(num)
        new_str = ''
        while k:
            for i in range(len(num)):
                # val = int(num[i]) - 0
                if i == len(num) - 1:#最后一个
                    k -= 1
                    del num[i]
                    break
                # elif i < len(num) - 1:
                else:
                    if num[i] > num[i+1]:
                        k -= 1
                        del num[i]
                        break
                    else:
                        continue

                # print('val:',val)
                if k == 0:
                    break
        #善后，除0
        start = 0
        for i in range(len(num)):
            if num[i] != '0':
                start = i
                break
        else:
            return '0'
        for i in range(start,len(num)):
            new_str += str(num[i])
        return new_str
# 栈的结构能解决回头问题，就是我一次循环到最后，k还有多余，需要回头删元素，这就靠栈
    def removeKdigits_v1(self, num, k):
        num = list(num)
        stack = []
        new_str = ''
        for i in range(len(num)):
            print('num[i]:',num[i])
            if stack != []:
                top = stack[-1]
                print('top:',top)
                while num[i] < top and k > 0:
                    stack.pop()
                    k -= 1
                    if stack == []:
                        break
                    top = stack[-1]
                    # continue#如果后者比前者小，应该持续弹栈，而不是紧接着入栈#这直接用continue不好做循环，容易丢最后的入栈,不如直接嵌套while小循环
            stack.append(num[i])


            # if k == 0:#这样break会导致进栈不充分
            #     break
        print('stack:',stack,' k :',k)
        while k:
            stack.pop()
            k -= 1
        # print('stack:',stack)
        #善后，除0
        start = 0
        for i in range(len(stack)):
            if stack[i] != '0':
                start = i
                break
        else:
            return '0'
        for i in range(start,len(stack)):
            new_str += str(stack[i])
        return new_str
    def removeKdigits(self, num, k):
        stack = []
        for i in range(len(num)):#不del，只遍历，也就不用转list了
            while stack != [] and num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            #关于0的处理，空栈不插0,数字不是0，栈不是空，至少满足一样
            if (num[i] != '0') or (stack != []):#注意python的转换，list中的仍然是字符
            # if not stack and n == '0': continue  # 他这个判断反过来写，看起来更清晰，如果空栈插0，continue跳过
                stack.append(num[i])#这样搞以后，不够出栈了
        while k and stack != []:#所以这里强行加了个判断，逻辑保持一致性，只能说套路不一样
            stack.pop()
            k -= 1
        return ''.join(stack) if stack else '0'


    def removeKdigits_others2(self, num, k):
        res = ''
        n = len(num)
        keep = n - k
        for c in num:
            while k and res and res[-1] > c:
                res = res[:-1]
                k -= 1
            res += c
        print(res)
        while res and res[0] == '0':
            res = res[1:]
        res = res[:keep]
        return res if res else '0'


# 如果只用一个条件，就是比后边都大，会有一个问题，一次循环不一定能达到k个。而且按同样的循环，下一次也不会有任何变化。
# example:"123454",k = 3
#倒是可以解决，就是后边没有的时候，删自身,就是得循环接近k次


num = '100'
k = 1
num = '112'
k = 1

num = "1432219"
k = 3
# 输出: "1219"

num = "1234567890"
k = 9

num = '10'
k = 2
num = "10200"#1比0大，所以删1，这个倒是还符合规则，就是要处理一下开头的0
k = 1
# 输出: "200"
sol = Solution()
print('ret:',sol.removeKdigits(num,k))

# l = [1,2,3,4,5]
# for i in range(len(l)):
#     print(l[i])
#     if l[i] == 3:
#         del l[i]




