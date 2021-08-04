class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sol (l1,l2) :
    l = []
    if l1 == None and l2 == None :
        return None
    if l1 == None and l2 != None :
        return l2
    if l1 != None and l2 == None :
        return l1

    while l1 != None and l2 != None :
        if l1.val < l2.val :
            l.append(l1.val)
            l1 = l1.next
        else :
            l.append(l2.val)
            l2 = l2.next

    op = ListNode(l[0])
    l = l[1::]
    tail = op

    for i in l :
        tail.next = ListNode(i)
        tail = tail.next
    # printListNode(op)
    if l1 != None :
        tail.next = l1
    else :
        tail.next = l2
    
    return op

def getListNode () :
    x = input()
    if x == '[]' :
        return ListNode()
    
    x = list(map(int,x.strip('[]').split(',')))
    head = ListNode(x[0])
    cur = head
    x = x[1::]
    for i in x :
        cur.next = ListNode(i)
        cur = cur.next
    return head

def printListNode (l) :
    print('[',end='')
    while l != None :
        print(l.val,end = ',')
        l = l.next
    print(']')

if __name__ == "__main__" :
    l1 = getListNode()
    l2 = getListNode()
    # printListNode(l1)
    # printListNode(l2)
    printListNode(sol(l1,l2))