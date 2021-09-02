def sol (s,k) :
    ans = ''
    while s != '' :
        cur = s[:2*k:]
        s = s[2*k::]
        cur_len = len(cur)
        if cur_len < k :
            cur = cur[::-1]
        else :
            cur = (cur[:k:])[::-1] + cur[k::]
        ans += cur
    return ans


if __name__ == "__main__" :
    s = input().strip('"')
    k = int(input())
    print(sol(s,k))