def sol (emails) :
    ans = []
    for cur in emails :
        head , tail = cur.split('@')
        head = head.split('+')[0]
        head = ''.join(head.split('.'))
        # print(head,tail)
        if head+'@'+tail not in ans :
            ans.append(head+'@'+tail)
    return len(ans)

if __name__ == "__main__" :
    l = list( x.strip('"') for x in input().strip('[]').split(',') )
    # print(l)
    print(sol(l))