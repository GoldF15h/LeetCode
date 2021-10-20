# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def checkLen (node,l=0) :
    if node == None :
        return l
    else :
        return checkLen(node.next,l+1)
        
def getIndex (node,i,cur=0) :
    if cur == i :
        return node
    else :
        return getIndex(node.next,i,cur+1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        _len = checkLen(head)
        # print(_len)
        if _len % 2 == 0 :
            index = (_len/2)+1
        else :
            index = (_len+1)//2
        return getIndex(head,index-1)