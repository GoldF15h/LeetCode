def sol (n) :
    ans = 0
    power = 0
    final = n
    while n > 0 :
        if n % 10 == 0 :
            ans += 9 * (10**power)
            n -= 10
        elif n % 10 == 1:
            if n > 10 :
                ans += 9 * (10**power)
                n -= 11
        else :
            ans += (n%10-1) * (10**power)
            
        n //= 10
        power += 1
    return [final-ans,ans]

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))
