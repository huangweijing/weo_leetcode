from typing import List
from collections import defaultdict, deque
from datetime import time
import datetime


class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        ans = []
        ac_dict = defaultdict(lambda : list[int]())
        for access in access_times:
            ac_dict[access[0]].append(access[1])
        for key in ac_dict.keys():
            ac_dict[key].sort()
            ac_queue = deque()
            for i, time_log in enumerate(ac_dict[key][1: ], start=1):
                hour = int(time_log[: 2])
                minute = int(time_log[2: ])
                last_time_hour = int(ac_dict[key][i - 1][:2])
                last_time_minute = int(ac_dict[key][i - 1][2: ])
                cur_time = datetime.datetime(year=2023, month=11, day=12,
                                             hour=hour, minute=minute, second=0)
                last_time = datetime.datetime(
                    year=2023, month=11, day=12,
                    hour=last_time_hour, minute=last_time_minute, second=0)
                ac_queue.append((cur_time - last_time).seconds)
                if len(ac_queue) > 2:
                    ac_queue.popleft()
                if len(ac_queue) == 2 and sum(ac_queue) < 3600:
                    ans.append(key)
                    break
        return ans


                # print(key, cur_time, last_time, cur_time - last_time, (cur_time - last_time).seconds)

access_times = [["a","0549"],["b","0457"],["a","0449"],["a","0621"],["b","0540"],["b", "0556"]]
r = Solution().findHighAccessEmployees(access_times)
print(r)
# print(datetime.datetime(hour=11, minute=30, second=0))
# datetime.datetime.now().minute=30
# print(time(11, 30, 0).time(10, 30, 0))


