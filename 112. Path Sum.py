# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _sum (cur,s,t) :

    if cur == None :
        return False
    
    if cur.left == None and cur.right == None :
        if s + cur.val == t :
            return True
        else :
            return False
        
    if cur.left != None and cur.right == None :
        return _sum(cur.left,s + cur.val,t)
        
    if cur.left == None and cur.right != None :
        return _sum(cur.right,s + cur.val,t)
        
    return _sum(cur.left,s + cur.val,t) or _sum(cur.right,s + cur.val,t)
        

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return _sum(root,0,targetSum)