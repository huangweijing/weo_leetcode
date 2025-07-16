class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        ans = []
        while idx1 < len(word1) or idx2 < len(word2):
            # print(idx1, idx2)
            if idx1 == len(word1):
                ans.append(word2[idx2:])
                break
            elif idx2 == len(word2):
                ans.append(word1[idx1: ])
                break
            if word1[idx1] > word2[idx2]:
                ans.append(word1[idx1])
                idx1 +=1
            else:
                ans.append(word2[idx2])
                idx2 += 1
            # print(ans)
        return "".join(ans)
    
data = [
    "cccbbd"
    , "dccba"
]
r = Solution().largestMerge(*data)
print(r)
