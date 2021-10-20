class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        emptyBottles = numBottles
        numBottles = 0
        while emptyBottles >= numExchange :
            
            numBottles = emptyBottles//numExchange
            emptyBottles = emptyBottles%numExchange
            
            ans += numBottles
            
            emptyBottles += numBottles
            
            
        return ans