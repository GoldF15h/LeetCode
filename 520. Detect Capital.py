def sol (word) :
    if word.isupper() :
        return True
    if word.islower() :
        return True
    if word[0].isupper() and word[1::].islower() :
        return True
    return False

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))