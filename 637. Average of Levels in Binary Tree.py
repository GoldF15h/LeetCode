# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

l = []
def getLevel (node,lv,cur=0) :
    global l
    if node != None :
        if lv == cur :
            l.append(node.val)
        else :
            getLevel(node.left,lv,cur+1)
            getLevel(node.right,lv,cur+1)

def getDepth(node,d=0) :
    if node == None :
        return d
    return max( getDepth(node.left,d+1) , getDepth(node.right,d+1) )

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        global l
        ans = []
        for i in range(getDepth(root)) :
            l = []
            getLevel(root,i)
            ans.append(sum(l)/len(l))
        return ans