from collections import Counter

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        left = Counter()
        right = Counter(customers)
        ans, min_penalty = -1, right["Y"]
        for i, cust in enumerate(customers):
            left[cust] += 1
            right[cust] -= 1
            penalty = left["N"] + right["Y"]
            if penalty < min_penalty:
                ans, min_penalty = i, penalty
        return ans + 1
