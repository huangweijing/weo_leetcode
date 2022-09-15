from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return day_of_week[date(year, month, day).weekday()]

r = Solution().dayOfTheWeek(11, 9, 2022)
print(r)