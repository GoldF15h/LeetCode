# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
op = 0
def left_sum(node,isLeft) :
    global op
    if node != None :
        left_sum(node.left,True)
        left_sum(node.right,False)
        if node.left == None and node.right == None and isLeft :
            op += node.val
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        global op
        op = 0
        left_sum(root,False)    
        return op