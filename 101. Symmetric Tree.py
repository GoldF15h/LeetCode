# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def leftPre (r,op) :
    if r != None :
        op.append(r.val)
        leftPre(r.left,op)
        leftPre(r.right,op)
    else :
        op.append(-1)
        
def leftIn (r,op) :
    if r != None :
        leftIn(r.left,op)
        op.append(r.val)
        leftIn(r.right,op)
    else :
        op.append(-1)
        
def leftPost (r,op) :
    if r != None :
        leftPost(r.left,op)
        leftPost(r.right,op)
        op.append(r.val)
    else :
        op.append(-1)

def rightPre(r,op) :
    if r != None :
        op.append(r.val)
        rightPre(r.right,op)
        rightPre(r.left,op)
    else :
        op.append(-1)
        
def rightIn(r,op) :
    if r != None :
        rightIn(r.right,op)
        op.append(r.val)
        rightIn(r.left,op)
    else :
        op.append(-1)
        
def rightPost(r,op) :
    if r != None :
        rightPost(r.right,op)
        rightPost(r.left,op)
        op.append(r.val)
    else :
        op.append(-1)
        
def isSameTree (rootL,rootR) :
    _rootL = []
    _rootR = []
    leftPre(rootL,_rootL)
    rightPre(rootR,_rootR)
    if _rootL != _rootR :
        return False
    
    _rootL = []
    _rootR = []
    leftIn(rootL,_rootL)
    rightIn(rootR,_rootR)
    if _rootL != _rootR :
        return False
    
    _rootL = []
    _rootR = []
    leftPost(rootL,_rootL)
    rightPost(rootR,_rootR)
    if _rootL != _rootR :
        return False
    
    return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return isSameTree(root.left,root.right)
        