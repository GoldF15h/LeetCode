class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1 :
            x = stones[-2]
            y = stones[-1]
            stones.pop()
            stones.pop()
            if x != y :
                y = y - x
                stones.append(y)
                stones.sort()
        if stones == [] :
            return 0
        return stones[0]