class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        h = len(matrix)
        w = len(matrix[0])
        ans = []
        
        for curCol in range(w) :
            tmp = []
            for curRow in range(h) :
                tmp.append(matrix[curRow][curCol])
            ans.append(tmp)
            
        return ans
                
            