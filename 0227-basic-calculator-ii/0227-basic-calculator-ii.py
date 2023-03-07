class Solution:
    def calculate(self, s: str) -> int:
        currNumber = 0
        
        currOperator = "+"
        
        stack = []
        
        numbers = [str(i) for i in range(0, 10)]
        
        operators = ["+", "-", "*", "/"]
        
        for i in range(len(s)):
            currChar = s[i]
            
            if currChar in numbers:
                currNumber = currNumber * 10 + int(currChar)
                
            if currChar in operators or i == len(s) - 1:
                if currOperator == "+":
                    stack.append(currNumber)
                    
                elif currOperator == "-":
                    stack.append(-currNumber)
                    
                elif currOperator == "*":
                    stack[-1] = stack[-1] * currNumber
                    
                elif currOperator == '/':
                    stack[-1] = int(stack[-1] / currNumber)
                    
                currNumber = 0
                
                currOperator = currChar
                
        result = 0
        for num in stack:
            result += num
            
        return result