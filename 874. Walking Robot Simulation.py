def sol (commands,obstacles) :
    x = 0
    y = 0
    facingDegree = 90
    ans = 0
    for curCommand in commands :
        # turn left
        if curCommand == -1 :
            facingDegree -= 90
            if facingDegree < 0 :
                facingDegree += 360
        # turn right
        elif curCommand == -2 :
            facingDegree += 90
            if facingDegree > 360 :
                facingDegree -= 360
        else :
            # บน
            if facingDegree == 0 :
                for i in range(curCommand) :
                    if [x,y+1] in obstacles :
                        break
                    else :
                        y += 1
            # ขวา
            elif facingDegree == 90 :
                for i in range(curCommand) :
                    if [x+1,y] in obstacles :
                        break
                    else :
                        x += 1
            # ซ้าย
            elif facingDegree == 180 :
                for i in range(curCommand) :
                    if [x-1,y] in obstacles :
                        break
                    else :
                        x -= 1
            # ล่าง
            elif facingDegree == 270 :
                for i in range(curCommand) :
                    if [x,y-1] in obstacles :
                        break
                    else :
                        y -= 1
        ans = max(ans,x**2 + y**2)
    return ans

if __name__ == "__main__" :
    c = list(map(int,input().strip('[]').split(',')))
    o = list( list(map(int,x.split(','))) for x in input().strip('[]').split('],[') )
    print(sol(c,o))