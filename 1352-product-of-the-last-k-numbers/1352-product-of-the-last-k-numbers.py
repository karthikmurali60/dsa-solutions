class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.product = 1
        
    def add(self, num: int) -> None:
        if num != 0:
            self.product *= num
            self.arr.append(self.product)
        else:
            self.product = 1
            self.arr = []

    def getProduct(self, k: int) -> int:
        # This case happens if a zero was added to the stream
        if len(self.arr) < k:
            return 0
        elif len(self.arr) == k:
            return self.arr[-1]
        else:
            return self.arr[-1] // self.arr[-1-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)