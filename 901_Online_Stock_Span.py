class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        span = 1
        while len(self.stk) > 0 and self.stk[-1][0] <= price:
            pre_span = self.stk.pop()
            span += pre_span[1]
        self.stk.append([price, span])
        return span



