class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 < 5:
            purchaseAmount = (purchaseAmount // 10) * 10
        else:
            purchaseAmount = (purchaseAmount // 10 + 1) * 10

        return 100 - purchaseAmount

r = Solution().accountBalanceAfterPurchase(45)
print(r)