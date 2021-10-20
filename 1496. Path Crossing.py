class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = [[0,0]]
        x = 0
        y = 0
        for o in path :
            if o == 'N' :
                y += 1
            if o == 'S' :
                y -= 1
            if o == 'E' :
                x += 1
            if o == 'W' :
                x -= 1
                
            if [x,y] in visit :
                    return True
            else :
                visit.append([x,y])
                
        return False