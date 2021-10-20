def sol (sentence) :
    op = []
    vowels = ['a','A','e','E','i','I','o','O','u','U']
    add_tail = 'a'
    for cur in sentence.split() :
        if cur[0] in vowels :
            op.append( cur + 'ma' + add_tail )
        else :
            op.append( cur[1::] + cur[:1:] + 'ma' + add_tail)
    add_tail += 'a'
    return ' '.join(op)

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))