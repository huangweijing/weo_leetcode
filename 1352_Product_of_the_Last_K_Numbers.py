class ProductOfNumbers:

    def __init__(self):
        self.prod_sum = [1]
        self.zero_idx = -1
        

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_idx = len(self.prod_sum)
            self.prod_sum.append(1)
        else:
            self.prod_sum.append(self.prod_sum[-1] * num)

    def getProduct(self, k: int) -> int:
        right = len(self.prod_sum) - 1
        left = len(self.prod_sum) - k - 1
        if self.zero_idx > left:
            return 0
        else:
            return self.prod_sum[right] // self.prod_sum[left]

        
obj = ProductOfNumbers()
obj.add(4)
obj.add(9)
obj.add(0)
obj.add(9)
obj.add(3)
print(obj.getProduct(2))

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)