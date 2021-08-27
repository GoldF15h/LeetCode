def sol (pattern,s) :
    _len = len(pattern)
    s = s.split()
    if _len != len(s) :
        return False

    pattern_stack = []
    s_stack = []
    
    for i in range(_len) : 
        if pattern[i] not in pattern_stack :
            pattern_stack.append(pattern[i])
            if s[i] not in s_stack :
                s_stack.append(s[i])
            else :
                return False
        else :
            cur_index = pattern_stack.index(pattern[i])
            if s_stack[cur_index] != s[i] :
                return False

    return True

if __name__ == "__main__" :
    pattern = input().strip('"')
    s = input().strip('"')
    print(sol(pattern,s))