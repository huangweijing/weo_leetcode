from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.price_table = {
            p: prices[i] for i, p in enumerate(products)
        }
        self.discount = discount
        self.customer_cnt = 0


    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_cnt += 1
        bill = 0
        for i, p in enumerate(product):
            price = self.price_table[p]
            bill += price * amount[i]
        if self.customer_cnt % self.n == 0:
            bill *= (100 - self.discount) / 100
        return bill

        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)