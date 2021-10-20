def isBSubStrA (a,b) :
    for i in range(len(a)-len(b)+1) :
        if a[i] == b[0] :
            isSub = True
            for j in range(len(b)) :
                if a[i+j] != b[j] :
                    isSub = False
                    break
            if isSub :
                return True
    return False

def sol (words) :
    ans = []
    words.sort(key = len)
    for i in range(len(words)-1) :
        for j in range(i+1,len(words)) :
            if isBSubStrA(words[j],words[i]) :
                if words[i] not in ans :
                    ans.append(words[i])
    return ans

# ["mass","as","hero","superhero"]
if __name__ == "__main__" :
    l = list( x.strip('"') for x in input().strip('[]').split(',') )
    # print(l)
    print(sol(l))
    # print(isBSubStrA('asd','aa'))