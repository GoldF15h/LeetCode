def sol(s) :
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    _len = len(s)
    left = 0
    right = _len-1
    s = list(s)
    while left < right :
        while left < _len and s[left] not in vowels :
            left += 1
        while 0 <= right and s[right] not in vowels :
            right -= 1
        if left >= right :
            break
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    return ''.join(s)
         

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))