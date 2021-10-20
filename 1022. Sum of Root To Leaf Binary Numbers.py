# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

ans = 0

def traverse (node,cur=0) :
    if node != None :
        cur = cur*2 + node.val
        if node.left != None or node.right != None :
            traverse (node.left,cur)
            traverse (node.right,cur)
        else :
            global ans
            ans += cur
    
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        traverse(root)
        return ans