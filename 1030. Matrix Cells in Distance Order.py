class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        l = []
        for curRow in range(rows) :
            for curCol in range(cols) :
                dis = ( abs(curRow - rCenter) + abs(curCol -cCenter) )
                # print('[',curRow,curCol,']',dis)
                l.append([ dis, [curRow,curCol] ])
        # print(l)
        l.sort()
        # for i in range(len(l)) :
        #     for j in range(len(l)-i-1) :
        #         if l[j] >= l[j+1] :
        #             l[j] , l[j+1] = l[j+1] , l[j]
        # print(l)
        return list( x[1] for x in l )