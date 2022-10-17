class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        numberOfElementsPopped = 0
        
        for element in pushed:
            stack.append(element)
            
            while(stack and numberOfElementsPopped <= len(pushed) and stack[-1] == popped[numberOfElementsPopped]):
                stack.pop()
                numberOfElementsPopped += 1
        
        return numberOfElementsPopped == len(pushed)