from typing import List

class Solution:
    def read_hour(self, hours: set[int], turned_on: int) -> set[int]:
        if turned_on == 0:
            return {0}
        result = set[int]()
        for hour in hours:
            copy_hours = hours.copy()
            copy_hours.remove(hour)
            result_n_1 = self.read_hour(copy_hours, turned_on - 1)
            for comb in result_n_1:
                if comb + hour <= 11:
                    result.add(comb + hour)
        return result

    def read_mins(self, mins: set[int], turned_on: int) -> set[int]:
        if turned_on == 0:
            return {0}
        result = set[int]()
        for minute in mins:
            copy_mins = mins.copy()
            copy_mins.remove(minute)
            result_n_1 = self.read_mins(copy_mins, turned_on - 1)
            for comb in result_n_1:
                if comb + minute <= 59:
                    result.add(comb + minute)
        return result

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hour_set = {1, 2, 4, 8}
        min_set = {1, 2, 4, 8, 16, 32}
        result = list[str]()
        for i in range(turnedOn + 1):
            hour_result = self.read_hour(hour_set, i)
            # if len(hour_result) == 0:
            #     hour_result.add(0)
            min_result = self.read_mins(min_set, turnedOn - i)
            # if len(min_result) == 0:
            #     min_result.add(0)
            for hour in hour_result:
                for minute in min_result:
                    result.append(f"{hour}:{str(minute).zfill(2)}")
        return result

# t = dict()
# # dict get default key value
# print(t.get("t", "abd"))
