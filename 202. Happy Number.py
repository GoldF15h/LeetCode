def sol (n) :
    passed_number = []
    while n != 1 :
        if n in passed_number :
            return False
        passed_number.append(n)
        split = []
        tmp = n
        n = 0 
        while tmp > 0 :
            n += (tmp%10)**2
            tmp //= 10
    return True

if __name__ == "__main__" :
    n = int(input())
    print(sol(n))