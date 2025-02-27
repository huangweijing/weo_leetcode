from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        even_list, odd_list = [], []
        for val in cnt.values():
            if val & 1 == 0:
                even_list.append(val)
            else:
                odd_list.append(val)
        even_list.sort()
        odd_list.sort()
        return odd_list[-1] - even_list[0]
    
