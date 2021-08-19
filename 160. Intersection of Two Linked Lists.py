# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getLen (node) :
    _len = 0
    while node != None :
        node = node.next 
        _len = _len + 1
    return _len

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        A = []
        
        intersectVal = 0
        listA = headA
        listB = headB
        skipA = 0
        skipB = 0
        
        lenA = getLen(listA)
        lenB = getLen(listB)
        isSwap = False
        
        if lenA < lenB :
            isSwap = True
            listA,listB = listB,listA
            lenA,lenB = lenB,lenA
        
        while lenA > lenB :
            if listA == listB :
                intersectVal = listA.val
                return listA
            
            lenA = lenA - 1 
            listA = listA.next
            skipA = skipA + 1

        while listA != None :
            if listA == listB :
                if isSwap :
                    listA,listB = listB,listA
                    skipA,skipB = skipB,skipA
                intersectVal = listA.val
                return listA

            listA = listA.next
            skipA = skipA + 1
            listB = listB.next
            skipB = skipB + 1