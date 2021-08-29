# def sol (s) :
#     d = {}
#     for cur in s :
#         if d.get(cur) :
#             d[cur] += 1
#         else :
#             d.update({cur:1})
#     l = list(d.values())
#     print(d)
#     _min = min(l)

#     if _min == 1 :
#         return False

#     pattern_len = 0
#     _len = len(l)
#     for i in range(_len) :
#         if l[i] % _min == 0 :
#             pattern_len += l[i]//_min
#         else :
#             return False
#     pattern = s[:pattern_len:]
#     print(pattern)
#     for i in range(0,len(s),pattern_len) :
#         if pattern != s[i:i+pattern_len:] :
#             return False
#     return True

def sol (s) :
    _len = len(s)
    isAns = False
    for i in range(1,(_len//2)+1) :
        pattern = s[:i:]
        # print(pattern)
        isAns = True
        for j in range(0,_len,i) :
            cur = s[j:j+i:]
            if pattern != cur :
                isAns = False
                break
        if isAns :
            return True
    return False


if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))