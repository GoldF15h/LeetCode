def isPalindrome (s) :
    _len = len(s)
    front = 0 
    back = _len - 1
    while front < back :
        if s[front] != s[back] :
            return False
        front += 1
        back -= 1
    return True


def sol (s) :
    if isPalindrome(s) :
        return True

    _len = len(s)
    front = 0
    back  = _len - 1
    
    while front < back :
        # print(front,back)
        if s[front] != s[back] :
            cut_front = s[:front:] + s[front+1::]
            cut_back = s[:back:] + s[back+1::]
            # print(cut_front,cut_back)
            if isPalindrome(cut_front) or isPalindrome(cut_back):
                return True
            else :
                return False
        front += 1
        back -= 1
    return False

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))