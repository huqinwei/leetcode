class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # n = len(s)
        # left = '({['
        # stack = []
        # for i in s:
        #     # print(i)
        #     if i in left:
        #         stack.append(i)
        #     elif len(stack) == 0:
        #         return False
        #     else:
        #         if i == ')' and stack[-1] == '(' or i == ']' and stack[-1] == '[' or i == '}' and stack[-1] == '{' :
        #             stack.pop()
        #         else:
        #             return False
        # if stack == []:
        #     return True
        #
        # return False

        # 我的peek操作有点多
        #########################################################
        # stack = []
        # for i in s:
        #     if i in '({[':
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         c = stack.pop()
        #         if i == ')' and c != '(' or i == ']' and c != '[' or i == '}' and c != '{':
        #             return False
        # return not stack

        # 执行一次pop，同样慢
        #########################################################
        # stack = []
        # for i in s:
        #     if i in '({[':
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         c = stack.pop()
        #         if i == ')' and c != '(':
        #             return False
        #         if i == ']' and c != '[':
        #             return False
        #         if i == '}' and c != '{':
        #             return False
        # return not stack
        # 反而更慢
        #########################################################
        # stack = []
        # for i in s:
        #     if i in '({[':
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         c = stack.pop()
        #         if i == ')':
        #             if c != '(':
        #                 return False
        #         if i == ']':
        #             if c != '[':
        #                 return False
        #         if i == '}':
        #             if c != '{':
        #                 return False
        # return not stack
        # 可能是网站自身问题
        #########################################################

        # 完整复制更快代码也没变快，可能是网站自身问题
        t=[]
        for w in s:
            if w in ('(','[','{'):
                t.append(w)
            else:
                if not t:
                    return False
                c=t.pop()
                if w==')':
                    if c!='(':
                        return False
                if w==']':
                    if c!='[':
                        return False
                if w=='}':
                    if c!='{':
                        return False
        return not t
        #########################################3


s = Solution()
print(s.isValid("(])"))


# stack = []
# stack.append('[')
# print(stack)
# # stack.remove('[')
# print(stack[-1])
# print('pop:',stack.pop())
# print(stack)
# print(stack==[])
# print(not stack)
# print(0 == len(stack))