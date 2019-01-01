
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':#重点是这块，pop操作
                # curstring是一直维护的逐渐增大的return string，每次遇到新的[把旧的存入stack，顺便用栈记住当前num，然后累加
                prenum = stack.pop()#prenum虽然描述很不“恰当”，但是curnum被另一个占用了，就是当前累计的数字，主要是变量用的太紧凑造成的
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():#看一下数字的处理方法，前一个当前数字乘以10，加下一个当前数字
                curnum = curnum * 10 + int(char)
            else:
                curstring += char
                # 其实他把curstring用final_string和一个tmp分开不就好了？
                # 好像暴露问题了，按他的这种逻辑，是区分不出一个没有[]包裹的字符和有[]包裹的字符的
            # print('stack:',stack)
            # print('curstring:',curstring)
        return curstring

    # 自己的改版，应付普通输入没问题，但是他有这种输入    "3[a2[c]]"
    def decodeString_failed(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        final_string = ''
        curstring = ''
        in_brackets = False
        for char in s:
            if char == '[':
                curstring = ''
                in_brackets = True
            elif char == ']':
                final_string = final_string + curnum * curstring
                in_brackets = False
                curnum = 0
            elif char.isdigit():#看一下数字的处理方法，前一个当前数字乘以10，加下一个当前数字
                curnum = curnum * 10 + int(char)
            else:
                if in_brackets:
                    curstring += char
                else:
                    final_string += char
        return final_string

s = Solution()
print(s.decodeString('2[abc]3[cd]ef'))

#
# s = '123'
# sum = 1 + int(s)
# print(sum)
#
# s = ['1','2']
# print(int(s))

