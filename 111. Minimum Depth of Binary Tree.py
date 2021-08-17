# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def Min_depth (c,h) :
    if c == None :
        return h
    if c.left == None and c.right == None :
        return h+1
    if c.left != None and c.right == None :
        return Min_depth(c.left,h+1)
    if c.left == None and c.right != None :
        return Min_depth(c.right,h+1)
    return min ( Min_depth(c.left,h+1),Min_depth(c.right,h+1))

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return Min_depth(root,0)