from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = 0
        waiting_time = 0
        for cust in customers:
            arrival, cook_time = cust[0], cust[1]
            finish_time = max(arrival, finish_time) + cook_time
            waiting_time += finish_time - arrival
        return waiting_time / len(customers)