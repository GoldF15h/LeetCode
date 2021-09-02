# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def get_depth(node,d):
    if node == None :
        # print('depth',d)
        return d
    return max( get_depth(node.left,d+1),get_depth(node.right,d+1) )

def get_path(node) :
    if node == None :
        # print("NONE")
        return 0
    op = get_depth(node.left,0) + get_depth(node.right,0)
    # print(op)
    return op

def traverse(node) :
    if node == None :
        return 0
    return max(traverse(node.left) ,get_path(node),traverse(node.right) )

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return traverse(root)