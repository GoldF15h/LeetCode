# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_depth (c,h) :
    if c != None :
        return max( max_depth(c.left,h+1), max_depth(c.right,h+1) )
    else :
        return h

def sub_tree(c) :
    if c != None :
        if abs(max_depth(c.left,0) - max_depth(c.right,0)) > 1 :
            return False
        else :
            return sub_tree(c.left) and sub_tree(c.right)
    else :
        return True
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return sub_tree(root)