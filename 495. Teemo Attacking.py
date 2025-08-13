class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration

        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration < timeSeries[i + 1]:
                total += duration
            else:
                total += timeSeries[i + 1] - timeSeries[i]

        return total
