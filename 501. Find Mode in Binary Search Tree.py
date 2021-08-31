# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

d = {}

def traverse (node) :
    global d
    if node != None :
        if d.get(node.val) :
            d[node.val] += 1
        else :
            d.update({node.val:1})
        traverse(node.left)
        traverse(node.right)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        global d
        d = {}
        op = []
        traverse(root)
        _max = max(list(d.values()))
        for i in d.keys() :
            if d[i] == _max :
                op.append(i)
        return op