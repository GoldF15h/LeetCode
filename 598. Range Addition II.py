class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for cur in ops :
            if cur[0] < m :
                m = cur[0]
            if cur[1] < n :
                n = cur[1]
        return m*n