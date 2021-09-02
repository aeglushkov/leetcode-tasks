class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        i = 0
        total_duration = duration
        while i < len(timeSeries) - 1:
            total_duration += min(timeSeries[i + 1] - timeSeries[i], duration)
            i += 1
        return total_duration
