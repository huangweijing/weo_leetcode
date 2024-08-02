class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_ang = (hour + minutes / 60) / 12 * 360
        min_ang = minutes / 60 * 360
        return min(abs(hour_ang - min_ang), 360 - abs(hour_ang - min_ang))