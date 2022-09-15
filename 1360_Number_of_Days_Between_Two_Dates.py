from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((date.fromisoformat(date2) - date.fromisoformat(date1)).days)

r = Solution().daysBetweenDates("2019-06-29", "2019-06-23")
print(r)
