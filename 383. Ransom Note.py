def sol(ransomNote,magazine) :
    ransomNote = list(ransomNote)
    d = {}
    for cur in magazine :
        if d.get(cur) :
            d[cur] += 1
        else :
            d.update({cur:1})

    for cur in ransomNote :
        if d.get(cur) :
            d[cur] -= 1
            if d[cur] == 0 :
                d.pop(cur)
        else :
            return False
    return True
            
if __name__ == "__main__" :
    a = input().strip('"')
    b = input().strip('"')
    print(sol(a,b))