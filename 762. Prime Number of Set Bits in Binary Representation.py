import math

def isPrime(n) :
    if n <= 1 :
        return False 
    for i in range(2,int(math.sqrt(n))+1,1) :
        if n % i == 0 :
            return False
    return True

def countSetBits(n) :
    op = 0
    while n > 0 :
        if n % 2 == 1 :
            op += 1
        n //= 2
    return op

def sol (left,right) :
    op = 0
    for i in range(left,right+1) :
        if isPrime(countSetBits(i)) :
            op += 1
    return op

if __name__ == "__main__" :
    a = int(input())
    b = int(input())
    print(sol(a,b))