class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        i = start 
        _sum = 0
        while i != destination :
            _sum += distance[i]
            i += 1
            if i >= len(distance) :
                i = 0
        
        ans = _sum
        
        i = start 
        _sum = 0
        while i != destination :
            i -= 1
            if i < 0 :
                i = len(distance) - 1
            _sum += distance[i]
        ans = min(_sum,ans)
        return ans
        
    z