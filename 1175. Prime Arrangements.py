def isPrime (n) :
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

def fac(n) :
    op = 1
    for i in range(n,1,-1) :
        op *= i
    return op

def sol (n) :
    nOfPrime = 0
    for i in range(1,n+1) :
        if isPrime(i) :
            nOfPrime += 1
    ans = fac(nOfPrime) * fac(n-nOfPrime)
    return ans % (10**9+7)
    
if __name__ == "__main__" :
    n = int(input())
    print(sol(n))