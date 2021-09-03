"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def depth(node,d) :
    if node.children == [] :
        return d+1
    _max = 0
    for cur in node.children :
        re = depth(cur,d+1)
        if re > _max :
            _max = re
    return _max

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None :
            return 0
        return depth(root,0)