def sol (s,k) :
    s = s.upper()
    s = ''.join(s.split('-'))
    if len(s)%k :
        ans = [s[:len(s)%k:]]
        s = s[len(s)%k::]
    else :
        ans = []
    for i in range(0,len(s),k) :
        ans.append(s[i:i+k:])
    return '-'.join(ans)

if __name__ == "__main__" :
    s = input().strip('"')
    k = int(input())
    print(sol(s,k))