class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        head = coordinates[0]
        defM = (head[0] - coordinates[1][0]) / (head[1] - coordinates[1][1]) if (head[1] - coordinates[1][1]) != 0 else float('inf')
        for i in range(1,len(coordinates)) :
            if head[1] - coordinates[i][1] != 0 :
                m = (head[0] - coordinates[i][0]) / (head[1] - coordinates[i][1])
            else :
                m = float('inf')
            if m != defM :
                return False
        return True