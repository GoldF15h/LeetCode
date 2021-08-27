def bitCount (n) :
    op = 0
    while n > 0 :
        if n%2 == 1 :
            op += 1
        n//=2
    return op
    

def sol(n) :
    op = []
    for i in range(n+1) :
        op.append(bitCount(i))
    return op

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))