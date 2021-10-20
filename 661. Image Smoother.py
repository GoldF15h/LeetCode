import math
def smoothXY(x,y,w,h,arr) :
    op = 0
    count = 0
    # print('\n\n\n',x,y)
    for rowIndex in range(x-1,x+2,1) :
        for colIndex in range(y-1,y+2,1) :
            if (0 <= rowIndex and rowIndex < h) and (0 <= colIndex and colIndex < w):
                # print(arr[rowIndex][colIndex],end=' ')
                op += arr[rowIndex][colIndex]
                count += 1
        # print()
    return math.floor(op/count)

def sol (img) :
    w = len(img[0])
    h = len(img)
    ans = []
    for i in range(h) :
        tmp = []
        for j in range(w) :
            tmp.append(smoothXY(i,j,w,h,img))
        ans.append(tmp)
    return ans
        
if __name__ == "__main__" :
    l = input().strip('[]').split('],[')
    l = list( list(map(int,x.split(','))) for x in l )
    # for i in l :
    #     print(i)
    print(sol(l))