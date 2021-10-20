# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []

def leafTraverse (node) :
    if node != None :
        if node.left == None and node.right == None :
            global l 
            l.append(node.val)
        else :
            leafTraverse(node.left)
            leafTraverse(node.right)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        global l 
        l = []
        leafTraverse(root1)
        leaf1 = l
        l = []
        leafTraverse(root2)
        leaf2 = l
        return leaf1 == leaf2