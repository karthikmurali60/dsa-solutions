class Solution:
    def isArmstrong(self, n: int) -> bool:
        numDigits = 0
        
        copy = anotherCopy = n
        
        while copy > 0:
            numDigits += 1
            copy = copy // 10
            
        armstrongSum = 0
        
        while anotherCopy > 0:
            digit = anotherCopy % 10
            armstrongSum += pow(digit, numDigits)
            anotherCopy = anotherCopy // 10
            
        return True if armstrongSum == n else False
