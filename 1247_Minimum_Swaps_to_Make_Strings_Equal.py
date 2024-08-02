from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt = Counter([ch + s2[i] for i, ch in enumerate(s1)])
        if (cnt["xy"] + cnt["yx"]) & 1 == 1:
            return -1
        cost1 = cnt["xy"] // 2 + cnt["yx"] // 2
        cost2 = cnt["xy"] % 2 + cnt["yx"] % 2
        return cost1 + cost2
    
r = Solution().minimumSwap("xxxy", "yyyx")
print(r)
        

            
            


            
        