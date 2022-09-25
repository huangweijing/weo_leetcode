from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        zero_str = "0" * n
        last_laser_cnt = 0
        result = 0
        for b in bank:
            if zero_str == b:
                continue
            laser_cnt = b.count("1")
            result += laser_cnt * last_laser_cnt
            last_laser_cnt = laser_cnt
        return result

data_bank = ["000","111","000"]
r = Solution().numberOfBeams(data_bank)
print(r)


