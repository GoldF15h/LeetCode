def isOverlap (s1,e1,s2,e2) :
    print(s1,e1,s2,e2)
    if s1 == s2 and e1 == e2 :
        return True
    # print(s1 < s2 and s2 < e1)
    # print(s1 < e2 and e2 < e1)
    # print(s2 < s1 and s1 < e2)
    # print(s2 < e1 and e1 < e2)
    return (s1 < s2 and s2 < e1) or (s1 < e2 and e2 < e1) or (s2 < s1 and s1 < e2) or (s2 < e1 and e1 < e2)
        

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1,r1y1,r1x2,r1y2 = rec1
        r2x1,r2y1,r2x2,r2y2 = rec2
        return isOverlap(r1x1,r1x2,r2x1,r2x2) and isOverlap(r1y1,r1y2,r2y1,r2y2)
