class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ch_set = set(jewels)
        return len([ch for ch in stones if ch in ch_set])

