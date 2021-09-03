# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

_sum = 0
def treeSum (node) :
    if node == None :
        return 0
    return node.val + treeSum(node.left) + treeSum(node.right)

def tilt(node) :
    global _sum
    if node != None :
        _sum += abs(treeSum(node.left)-treeSum(node.right))
        tilt(node.left)
        tilt(node.right)

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        global _sum
        _sum = 0
        tilt(root)
        return _sum