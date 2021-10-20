class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        for curRow in range(h) :
            val = matrix[curRow][0]
            i = 0
            while i < h-curRow and i < w :
                # print(curRow+i,i)
                if matrix[curRow+i][i] != val :
                    return False
                i += 1
        # print('pass')
        for curCol in range(w) :
            val = matrix[0][curCol]
            i = 0
            while i < h and i < w-curCol :
                if matrix[i][curCol+i] != val :
                    return False
                i += 1
        return True