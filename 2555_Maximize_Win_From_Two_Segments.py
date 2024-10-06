from typing import List
from collections import Counter


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        prize_cnt = Counter(prizePositions)
        left_cnt = Counter()
        right_cnt = Counter()
        key_list = list(sorted(prize_cnt.keys()))
        left, right = 0, 0
        while left < len(key_list):
            base_left = 0
            while right < len(key_list) and key_list[right] <= key_list[left] + k:
                best_left += prize_cnt[key_list[right]]
                right += 1
            left_cnt[left] = base_left
            base_left -= prize_cnt[key_list[left]]
            left += 1
        left, right = 0, 0