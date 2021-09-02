# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []

def traverse (node) :
    global l
    if node != None :
        l.append(node.val)
        traverse(node.left)
        traverse(node.right)
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global l
        l = []
        traverse(root)
        l.sort()
        _min = l[1]-l[0]
        for i in range(1,len(l)-1) :
            cur = l[i+1]-l[i]
            if cur < _min :
                _min = cur
        return _min