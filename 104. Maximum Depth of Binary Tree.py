# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Depth_find(c,h) :
    if c != None :
        return max( Depth_find(c.left,h+1),Depth_find(c.right,h+1) )
    else :
        return h

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return Depth_find(root,0)