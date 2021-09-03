class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        op = []
        l = []
        for cur in mat :
            l += cur
        # print(l)
        if len(l) != r*c :
            return mat
        for i in range(r) :
            new_row = l[i*c:(i*c)+c:]
            op.append(new_row)
        return op