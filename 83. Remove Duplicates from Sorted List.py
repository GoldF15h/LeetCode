class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _print(n) :
    print('[',end=' ')
    while n != None :
        print('{},'.format(n.val),end='')
        n = n.next
    print(']')

def sol (head) :
    # _print(head)
    cur = head
    while cur != None and cur.next != None :
        if cur.val == cur.next.val :
            cur.next = cur.next.next
            cur = head
        else :
            cur = cur.next
    return head


if __name__ == "__main__" :
    # [1,1,2]    
    l = list(map(int,input().strip('[]').split(',')))
    dummy = ListNode()
    cur = dummy
    for i in l :
        new = ListNode(i)
        cur.next = new
        cur = cur.next
    # _print(dummy)
    _print(sol(dummy.next))