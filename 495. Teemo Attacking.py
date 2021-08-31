class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = duration
        for i in range(len(timeSeries)-1) :
            if  timeSeries[i+1] - timeSeries[i] >= duration :
                ans += duration
            else :
                ans += timeSeries[i+1] - timeSeries[i]
        return ans