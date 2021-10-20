class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0 
        for curRow in range(len(grid)):
            for curCol in range(len(grid[curRow])) :
                if grid[curRow][curCol] < 0 :
                    ans += 1
        return ans