def sol(s,t) :

    s = list(s)
    s.sort()

    t = list(t)
    t.sort()

    return s == t
    

if __name__ == "__main__" :
    s = input().strip('"')
    t = input().strip('"')
    print(sol(s,t))