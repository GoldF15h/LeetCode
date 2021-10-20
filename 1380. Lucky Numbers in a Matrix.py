def transpostMatrix (m) :
    op = []
    for curCol in range(len(m[0])) :
        tmp = []
        for curRow in range(len(m)) :
           tmp.append(m[curRow][curCol])
        op.append(tmp)
    return op


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        _min = []
        for curRow in matrix :
            _min.append(min(curRow))
        m = transpostMatrix(matrix)
        _max = []
        for curRow in range(len(m)) :
            _max.append(max(m[curRow]))
        for curRow in range(len(matrix)) :
            for curCol in range(len(matrix[0])) :
                if matrix[curRow][curCol] == _min[curRow] and  matrix[curRow][curCol] == _max[curCol] :
                    ans.append(matrix[curRow][curCol])
        return ans
        
             
        
                