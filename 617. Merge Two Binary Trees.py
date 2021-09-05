# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeSum (ans,a,b) :
    ans.val = a.val + b.val 
    if a.left != None or b.left != None :
        if a.left != None and b.left != None :
            ans.left = TreeNode()
            treeSum(ans.left,a.left,b.left)
        elif a.left != None and b.left == None :
            ans.left = a.left
        elif a.left == None and b.left != None :
            ans.left = b.left
        
    if a.right != None or b.right != None :
        if a.right != None and b.right != None :
            ans.right = TreeNode()
            treeSum(ans.right,a.right,b.right)
        elif a.right != None and b.right == None :
            ans.right = a.right
        elif a.right == None and b.right != None :
            ans.right = b.right
            
            
def printTree(node,lv=0) :
    if node != None :
        printTree(node.right,lv+1)
        print('     '*lv , node.val)
        printTree(node.left,lv+1)
            
            
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 == None :
            return root2
        if root2 == None :
            return root1
        ans = TreeNode()
        treeSum(ans,root1,root2)
        # printTree(ans)
        return ans