"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
op = []
def preOrder (node) :
    global op
    if node != None :
        op.append(node.val)
        for cur in node.children :
            preOrder(cur)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        global op
        op = []
        preOrder(root)
        return op