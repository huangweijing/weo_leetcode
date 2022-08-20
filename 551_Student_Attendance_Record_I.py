class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_cnt = 0
        late_cnt = 0
        for ch in s:
            if ch == "A":
                absent_cnt += 1
                late_cnt = 0
                if absent_cnt >= 2:
                    return False
            elif ch == "L":
                late_cnt += 1
                if late_cnt >= 3:
                    return False
            else:
                late_cnt = 0
        return True
