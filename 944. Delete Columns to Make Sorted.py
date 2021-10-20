class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for curCol in range(len(strs[0])) :
            for curRow in range(len(strs)-1) :
                if strs[curRow][curCol] > strs[curRow+1][curCol] :
                    ans += 1
                    break
        return ans
           