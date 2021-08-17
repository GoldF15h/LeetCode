# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder (node,l) :
    if node != None :
        postorder(node.left,l)
        postorder(node.right,l)
        l.append(node.val)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        postorder(root,l)
        return l