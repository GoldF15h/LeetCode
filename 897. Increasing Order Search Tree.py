# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []
def inOrder (node) :
    if node != None :
        global l 
        inOrder(node.left)
        l.append(node.val)
        inOrder(node.right)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        global l 
        l = []
        inOrder(root)
        root = TreeNode()
        curNode = root
        for curVal in l :
            curNode.right = TreeNode(curVal)
            curNode = curNode.right
        return root.right