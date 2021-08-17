# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        rabbit = head
        turtle = head
        
        while rabbit != None  and turtle != None :
            
            try :
                rabbit = rabbit.next
                turtle = turtle.next.next
                if rabbit == turtle :
                    return True
            except :
                return False