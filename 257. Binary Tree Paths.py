# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traverse (node,path) :
    if node == None :
        return []

    # print(node.val,path,t)
    path += [node.val]
    if node.left == None and node.right == None :
        print('return',path)
        return ["->".join( str(x) for x in path )]
    
    left = traverse(node.left,path[::])
    right = traverse(node.right,path[::])
    op = []
    
    if left != [] :
        op += left
    if right != [] :
        op += right
        
    return op

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if root.left == None and root.right == None :
        #         return [str(root.val)]
        return traverse(root,[])    