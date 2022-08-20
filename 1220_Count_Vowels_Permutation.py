class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vow_cnt = [1] * 5
        # a -> 0, e -> 1, i -> 2, o -> 3, u -> 4
        for i in range(n - 1):
            new_vow_cnt = [0] * 5
            new_vow_cnt[0] = vow_cnt[1] + vow_cnt[2] + vow_cnt[4]
            new_vow_cnt[1] = vow_cnt[0] + vow_cnt[2]
            new_vow_cnt[2] = vow_cnt[1] + vow_cnt[3]
            new_vow_cnt[3] = vow_cnt[2]
            new_vow_cnt[4] = vow_cnt[2] + vow_cnt[3]
            vow_cnt[:] = new_vow_cnt[:]
        return sum(vow_cnt) % (10^9 + 7)




