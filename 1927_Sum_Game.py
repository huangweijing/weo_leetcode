from collections import Counter

class Solution:
    def sumGame(self, num: str) -> bool:
        cnt1 = Counter()
        cnt2 = Counter()
        name = "a"
        sum1, sum2 = 0, 0
        for i, val in enumerate(num):
            if i < (len(num) >> 1):
                if val == "?":
                    cnt1[name] += 1
                    name = "b" if name == "a" else "a"
                else:
                    sum1 += int(val)
            else:
                if val == "?":
                    cnt2[name] += 1
                    name = "b" if name == "a" else "a"
                else:
                    sum2 += int(val)
        if cnt1["a"] > cnt2["b"]:
            cnt1["a"] -= cnt2["b"]
        else:
            cnt2["b"] -= cnt1["a"]
            
        