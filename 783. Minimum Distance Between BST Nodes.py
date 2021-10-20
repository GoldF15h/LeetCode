# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []
def traverse(node) :
    if node != None :
        global l
        l.append(node.val)
        traverse(node.left)
        traverse(node.right)
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        global l
        l = []
        traverse(root)
        l.sort()
        ans = l[1] - l[0]
        for i in range(len(l)-1) :
            cur = l[i+1] - l[i]
            if cur < ans :
                ans = cur
        return ans
        