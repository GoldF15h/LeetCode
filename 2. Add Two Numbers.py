# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        sum_l1 = 0
        cur_pow = 1
        while l1 != None :
            sum_l1 += l1.val * cur_pow
            cur_pow *= 10
            l1 = l1.next
        
        sum_l2 = 0
        cur_pow = 1
        while l2 != None :
            sum_l2 += l2.val * cur_pow
            cur_pow *= 10
            l2 = l2.next
            
        total = sum_l1 + sum_l2
        dummy = ListNode()
        cur = dummy
        if total == 0 :
            return ListNode(0)
        while total > 0 :
            cur.next = ListNode(total%10)
            cur = cur.next
            total //= 10
            
        return dummy.next