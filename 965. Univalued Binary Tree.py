# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

uni = -1
ans = False

def traverse (node) :
    if node != None :
        if node.val != uni :
            global ans
            ans = False
        traverse(node.left)
        traverse(node.right)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        global uni
        global ans
        ans = True
        uni = root.val
        traverse(root)
        return ans