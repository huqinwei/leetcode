# 示例 1：
#
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 示例 2：
#
# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 示例 3：
#
# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# 逆波兰表达式就是符号放后边的表达式，相对于传统写法，对计算机来说反而更好处理
# 大体规则就是从后向前，有了符号op就要找op1和op2，看起来op2就在栈顶，op1是之前计算的总和，看起来op1是需要先处理掉。
# 但是我也不确定他的具体规则和规律，比如，有没有(1+2)*(3+4)的形式呢？最好直接看答案了
# 注意：减法、除法都限制顺序的，top1明显是除数，不是被除数
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        oper = ['+', '-', '*', '/']
        for char in tokens:
            if char not in oper:
                stack.append(int(char))#cast
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                res = 0
                if char == '+':
                    res = top2 + top1
                elif char == '-':
                    res = top2 - top1
                elif char == '*':
                    res = top2 * top1
                elif char == '/':
                    res = top2 / top1
                stack.append(int(res))
        return stack.pop()


# class Solution:
#     def evalRPN(self, tokens):
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
#         import operator
#         stack = list()
#         ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
#         for char in tokens:
#             if char in ops:
#                 t1 = int(stack.pop())
#                 t2 = int(stack.pop())
#                 stack.append(ops[char](t2, t1))
#             else:
#                 stack.append(char)
#
#         return stack.pop()
s1 = Solution()
print('ret:',s1.evalRPN(["0","3","/"]))









