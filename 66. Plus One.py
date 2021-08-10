def sol(digits) :
    
    op = []
    digits[-1] = digits[-1] + 1
    digits = digits[::-1]
    
    for i in range(len(digits)-1) :
        # print( digits[:i:] , digits[i] , digits[i+1::] ,sep = '*')
        if digits[i] >= 10 :
            digits[ i+1 ]   =   digits[ i+1 ] + ( digits[i] // 10 )
            digits[i]       =   digits[i] % 10

    digits = digits[::-1]

    if digits[0] >= 10 :
        digits = [ digits[0]//10 ] + digits
        digits[1] = digits[1] % 10
        
    return digits
            
if __name__ == "__main__" :
    l =  list(map(int,input().strip('[]').split(',')))
    print(sol(l))