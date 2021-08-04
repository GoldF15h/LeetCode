def sol (strs) :
    
    shortest_word = ''
    _min = 201
    for i in strs :
        cur_len = len(i)
        if len(i) < _min :
            _min = cur_len
            shortest_word = i

    op = ''        
    for i in range(len(shortest_word)) :
        for j in strs :
            if shortest_word[i] != j[i] :
                return op
        op = op + shortest_word[i]
    return op


#  input = ["flower","flow","flight"]
if __name__ == "__main__" :
    n = input().strip('[]').split(',')
    n = list(x.strip('"') for x in n )
    print(sol(n))