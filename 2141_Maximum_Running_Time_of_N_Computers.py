from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        need_divide = sum(batteries[:-n])
        step_count = 1
        simultaneous_time = batteries[-n]
        if need_divide == 0:
            return simultaneous_time
        # print(f"need_divide={need_divide}, st={simultaneous_time}, batteries={batteries}")
        for i in range(len(batteries) - n + 1, len(batteries)):
            step_height = batteries[i] - batteries[i - 1]
            energy_needed = step_height * step_count
            # print(f"step_height={step_height}, energy_needed={energy_needed}"
            #       f", st={simultaneous_time}, need_divide={need_divide}")
            if energy_needed <= need_divide:
                need_divide -= energy_needed
                step_count += 1
                simultaneous_time += step_height
            else:
                simultaneous_time += need_divide // step_count
                need_divide = 0
                break
        simultaneous_time += need_divide // n
        return simultaneous_time

data = [
    4
    , [8, 12, 9, 77, 22]
]
r = Solution().maxRunTime(*data)
print(r)