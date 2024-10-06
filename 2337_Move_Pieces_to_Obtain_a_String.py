class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sr = start.replace("_", "")
        tr = target.replace("_", "")
        if sr != tr:
            return False
        # 1. left_cnt, right_cnt, ul_cnt
        cnt_arr = [[0] * 3 for _ in sr]
        ch_idx = 0
        ul_cnt, left_cnt, right_cnt = 0, 0, 0
        for ch in start:
            if ch == "L":
                cnt_arr[ch_idx] = [left_cnt, right_cnt, ul_cnt]
                left_cnt += 1
                ch_idx += 1
            elif ch == "_":
                ul_cnt += 1
            elif ch == "R":
                cnt_arr[ch_idx] = [left_cnt, right_cnt, ul_cnt]
                right_cnt += 1
                ch_idx += 1
        ch_idx = 0
        ul_cnt, left_cnt, right_cnt = 0, 0, 0
        for ch in target:
            if ch == "L":
                if cnt_arr[ch_idx][:2] != [left_cnt, right_cnt] or cnt_arr[ch_idx][2] < ul_cnt:
                    # print("aaa", [left_cnt, right_cnt, ul_cnt])
                    return False
                left_cnt += 1
                ch_idx += 1
            elif ch == "_":
                ul_cnt += 1
            elif ch == "R":
                # print(cnt_arr[ch_idx], [left_cnt, right_cnt, ul_cnt])
                if cnt_arr[ch_idx][:2] != [left_cnt, right_cnt] or cnt_arr[ch_idx][2] > ul_cnt:
                    return False
                right_cnt += 1
                ch_idx += 1
        return True
    

data = [
    "_R"
    , "R_"
]
r = Solution().canChange(* data)
print(r)
        