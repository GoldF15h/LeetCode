def sol(s) :
    s = s.strip().split(" ")
    return len(s[-1]) 

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))