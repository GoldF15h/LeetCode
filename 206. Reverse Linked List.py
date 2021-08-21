# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        stack = []
        cur = head
        while cur != None :
            stack.append(cur.val)
            cur = cur.next
        op_head = ListNode(stack[-1])
        cur = op_head
        stack.pop()
        while stack != [] :
            cur.next = ListNode(stack[-1])
            stack.pop()
            cur = cur.next
        return op_head
