class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        operator = "+"

        if not s:
            return 0

        operators = {'+','-','*','/'}
        nums = set(str(x) for x in range(0,10))

        for i in range(0,len(s)):
            char = s[i]

            if char in nums:
                curr = curr * 10 + int(char)

            if char in operators or i == len(s)-1:
                if operator == '+':
                    stack.append(curr)

                elif operator == '-':
                    stack.append(-curr)

                elif operator == '*':
                    stack[-1] *= curr

                elif operator == '/':
                    stack[-1] = int(stack[-1] / curr)

                curr = 0
                operator = char

        resultSum = 0
        for num in stack:
            resultSum += num
            
        return resultSum
        