class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a,b,c = points
        if a[0] == b[0] and b[0]  == c[0] :
            return False
        if a[1] == b[1] and b[1] == c[1] :
            return False
        if a == b or b == c or c == a :
            return False
        mSet = []
        for i in range(len(points)-1) :
            for j in range(i+1,len(points)) :
                
                if (points[i][1] - points[j][1]) != 0 :
                    m = (points[i][0] - points[j][0])/(points[i][1] - points[j][1])
                else : 
                    m = float('inf')
                # print(mSet)
                if m in mSet :
                    return False
                else :
                    mSet.append(m)
        return True