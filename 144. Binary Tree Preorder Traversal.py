# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder (node,l) :
    if node != None :
        l.append(node.val)
        preorder(node.left,l)
        preorder(node.right,l)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        preorder(root,l)
        return l