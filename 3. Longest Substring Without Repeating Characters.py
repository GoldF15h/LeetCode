def sol (s) :
    _len = len(s) 
    for checkRange in range(_len,0,-1) :
        for start in range(0,_len-checkRange+1) :
            curSubArr = s[start:start+checkRange]
            if len(set(curSubArr)) == len(curSubArr) :
                return checkRange
    return 0

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))