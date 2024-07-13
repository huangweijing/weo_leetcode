class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        k = 3
        alt_cnt_arr = [0] * len(colors)
        alt_cnt = 1
        for i, color in enumerate(colors):
            if color != colors[i - 1]:
                alt_cnt += 1
            else:
                alt_cnt = 1
            alt_cnt_arr[i] = alt_cnt
        for i in range(k):
            if colors[i] != colors[i - 1]:
                alt_cnt_arr[i] = alt_cnt_arr[i - 1] + 1
        # print(alt_cnt_arr)
        ans = 0
        for ele in alt_cnt_arr:
            if ele >= k:
                ans += 1
        return ans
    