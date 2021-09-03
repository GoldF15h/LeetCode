# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findSubNode (node,toFind,op) :
    if node != None :
        if node.val == toFind.val :
            op.append(node)
        left = findSubNode(node.left,toFind,op)
        right = findSubNode(node.right,toFind,op)
        
def inOrder (node,op) :
    if node != None :
        inOrder(node.left,op)
        op.append(node.val)
        inOrder(node.right,op)
            
def preOrder (node,op) :
    if node != None :
        op.append(node.val)
        preOrder(node.left,op)
        preOrder(node.right,op)
        
def postOrder (node,op) :
    if node != None :
        postOrder(node.left,op)
        postOrder(node.right,op)
        op.append(node.val)
        
def isTreeEq (a,b) :
        aL = []
        bL = []
        inOrder(a,aL)
        inOrder(b,bL)
        if aL != bL :
            return False
        
        aL = []
        bL = []
        preOrder(a,aL)
        preOrder(b,bL)
        if aL != bL :
            return False
        
        aL = []
        bL = []
        postOrder(a,aL)
        postOrder(b,bL)
        if aL != bL :
            return False
        
        return True
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodeList = []
        findSubNode(root,subRoot,nodeList)
        for curNode in nodeList :
            if isTreeEq(curNode,subRoot) :
                return True
        return False
        