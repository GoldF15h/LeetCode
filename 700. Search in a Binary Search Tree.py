# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeSearch (node,toFind) :
    if node == None :
        return None
    if node.val == toFind :
        return node
    if node.val > toFind :
        return treeSearch(node.left,toFind)
    else :
        return treeSearch(node.right,toFind)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return treeSearch(root,val)
        