# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

ans = ''
def traverse (node) :
    global ans
    if node != None :
        ans += str(node.val)
        if node.left != None and node.right != None :
            ans += '('
            traverse(node.left)
            ans += ')'
            ans += '('
            traverse(node.right)
            ans += ')'
        elif node.left != None and node.right == None :
            ans += '('
            traverse(node.left)
            ans += ')'
        elif node.left == None and node.right != None :
            ans += '()'
            ans += '('
            traverse(node.right)
            ans += ')'

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        global ans
        ans = ''
        traverse(root)
        return ans