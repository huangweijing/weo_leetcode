from datetime import date

class Solution:
    def dayOfYear(self, d: str) -> int:
        d1 = date.fromisoformat(d)
        d2 = date(d1.year, 1, 1)
        return (d1 - d2).days + 1
