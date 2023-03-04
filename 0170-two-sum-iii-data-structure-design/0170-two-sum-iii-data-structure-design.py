class TwoSum:
    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        hashMap = {}
        
        for num in self.arr:
            if value - num in hashMap:
                return True
            
            hashMap[num] = 1 + hashMap.get(num, 0)
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)