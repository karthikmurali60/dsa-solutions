class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = list(address)
        
        i = 0
        while i < len(l) - 1:
            if l[i + 1] == ".":
                l.insert(i + 1, "[")
                l.insert(i + 3, "]")
                i += 4
            else:
                i += 1
                
        return ''.join(l)