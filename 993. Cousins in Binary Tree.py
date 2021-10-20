# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

FindRe = None
def FindNode (node,toFind,d=0) :
    global FindRe
    if node != None :
        if node.left != None :
            if node.left.val == toFind :
                FindRe = [d+1,node]
                return
            else :
                FindNode(node.left,toFind,d+1)
        if node.right != None :
            if node.right.val == toFind :
                FindRe = [d+1,node]
                return
            else :
                FindNode(node.right,toFind,d+1)
        
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        global FindRe
        FindRe = None 
        FindNode(root,x)
        if FindRe == None :
            return False
        a = FindRe
        FindRe = None
        FindNode(root,y)
        if FindRe == None :
            return False
        b = FindRe
        FindRe = None
        return a[0] == b[0] and a[1] != b[1]