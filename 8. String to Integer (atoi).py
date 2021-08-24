def sol(s: str) -> int:
    s = s.strip()

    start = 0
    while not ( s[start].isnumeric() or s[start] == '-' ):
        start += 1

    end = len(s) - 1
    while not s[end].isnumeric() :
        end -= 1
    end += 1

    s = s[start:end]
    return int(s)

    

if __name__ == "__main__" :
    s = input().strip('"')
    print(sol(s))