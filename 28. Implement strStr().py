def ifSubSTR (a,b) :
    if a[:len(b):] == b :
        return True
    else :
        return False

def sol (haystack: str, needle: str) :

    if needle == '' :
        return 0
    if haystack == '' :
        return -1
    if len(haystack) < len(needle) :
        return -1
    if haystack == needle :
        return 0

    for i in range(len(haystack)) :
        if haystack[i] == needle[0] :
            if ifSubSTR(haystack[i::],needle) :
                return i

    return -1


if __name__ == "__main__" :
    s1 = input().strip('"')
    s2 = input().strip('"')
    print(sol(s1,s2))