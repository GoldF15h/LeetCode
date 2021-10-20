def sol (s) :
    curChr = ''
    curStart = 0
    ans = []
    for i in range(len(s)) :
        print(curChr,s[i])
        if curChr != s[i] :
            print('reset at i =',i)
            if i - curStart >= 3 :
                ans.append([curStart,i-1])
            curChr = s[i]
            curStart = i
    if len(s) - curStart >= 3 :
        ans.append([curStart,len(s)-1])
    return ans

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s)) 