class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        alp_cnt = [[0] * 26 for _ in word]
