def sol(s,t) :
    s_map = []
    t_map = []
    _len = len(s)
    for i in  range(_len):
        is_s_mapped = s[i] in s_map
        is_t_mapped = t[i] in t_map
        if not is_s_mapped and not is_t_mapped :
            s_map.append(s[i])
            t_map.append(t[i])
        elif is_s_mapped and is_t_mapped :
            if s_map.index(s[i]) != t_map.index(t[i]) :
                return False
        else :
            return False
    return True

if __name__ == "__main__":
    s = input().strip('"')
    t = input().strip('"')
    print(sol(s,t))