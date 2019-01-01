class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 不用穷举组合+剪枝+堆栈判断，直接设定规则来生成就行
        result = []

        def generate(left, right, s):
            if left == 0 and right == 0:
                result.append(s)
                return
            if left:
                generate(left - 1, right, s + '(')
            if left < right:
                generate(left, right - 1, s + ')')

        generate(n, n, '')
        return result

