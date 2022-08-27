class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(1, len(timeSeries)):
            interval = timeSeries[i] - timeSeries[i - 1]
            if interval < duration:
                result += interval
            else:
                result += duration
        result += duration
        return result

