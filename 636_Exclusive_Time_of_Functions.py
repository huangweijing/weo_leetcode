from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stk = []
        for log in logs:
            log_arr = log.split(":")
            log_id = int(log_arr[0])
            log_ts = int(log_arr[2])
            if log_arr[1] == "end":
                pop_item = stk.pop()
                start_log_ts = pop_item[0]
                duration = pop_item[1]

                ans[log_id] += log_ts - start_log_ts + 1 - duration
                if len(stk) > 0:
                    stk[-1][1] += log_ts - start_log_ts + 1
            else:
                stk.append([log_ts, 0])
            # print(log, stk)
        return ans
    

data = [
    1
    , ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
]
r = Solution().exclusiveTime(*data)
print(r)
                