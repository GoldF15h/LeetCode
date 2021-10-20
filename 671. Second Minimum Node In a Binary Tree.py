# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []
def secMin(node) :
    if node != None :
        global l 
        l.append(node.val)
        secMin(node.left)
        secMin(node.right)

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        global l
        l = []
        secMin(root)
        l = list(set(l))
        l.sort()
        if len(l) >= 2 :
            return l[1]
        return -1
        