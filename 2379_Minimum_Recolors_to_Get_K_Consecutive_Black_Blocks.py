from collections import Counter

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = k
        block_list = list(blocks)
        for i in range(len(block_list) - k + 1):
            cnt = Counter(block_list[i: i+k])
            result = min(cnt["W"], result)
        return result