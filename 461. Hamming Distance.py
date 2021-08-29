def toBi (n) :
    op = []
    while n > 0 :
        op.append(n%2)
        n//=2
    op = (op + [0]*(32-len(op)))[::-1]
    return op

def sol (x,y):
    lx = toBi(x)
    ly = toBi(y)
    ans = 0
    for i in range(32) :
        if lx[-1] != ly[-1] :
            ans += 1
        lx.pop()
        ly.pop()
    return ans

if __name__ == "__main__" :
    x = int(input())
    y = int(input())
    print(sol(x,y))