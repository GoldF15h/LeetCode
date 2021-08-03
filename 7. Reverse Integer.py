def sol (x) :
    x = str(x)
    if len(x) != 1 :
        x = x.strip('0')
        if (x[0] == '-') :
            x = x[1::]
            x = x[::-1]
            x = '-'+x
        else :
            x = x[::-1]
    if  int(x) in range(-2**31,2**31-1) :
        return x
    else :
        return 0
        
if __name__ == "__main__" :
    n = int(input())
    print(sol(n))