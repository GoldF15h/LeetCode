def sol(s,t) :
    if s == '' :
        return True
    if t == '' :
        return False
    
    cur_s = 0
    cur_t = 0
    s_len = len(s)
    t_len = len(t)

    while cur_t < t_len :
        if s[cur_s] == t[cur_t] :
            cur_s += 1
            if cur_s == s_len :
                return True
        cur_t += 1
    return False

if __name__ == "__main__" :
    s = input().strip('"')
    t = input().strip('"')
    print(sol(s,t))