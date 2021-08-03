def sol (s) :

    dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
    }

    s = list(s)
    for cur in range(len(s)) :
        s[cur] = dict[s[cur]]
    
    _sum = 0 

    for cur in range(len(s)) :
        try:
            if ( s[cur] < s[cur+1] ) :
                _sum = _sum - s[cur]
            else :
                _sum = _sum + s[cur]
        except :
            _sum = _sum + s[cur]

    return _sum

    

if __name__ == "__main__" :
    s = input()
    print(sol(s))