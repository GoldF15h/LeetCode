"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def postOrder(node,op) :
    if node != None :
        for cur in node.children :
            postOrder(cur,op)
        op.append(node.val)
        

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        op = []
        postOrder(root,op)
        return op