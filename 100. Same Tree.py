# ข้อนี้ก็เหมือนกับข้อที่ 94 เลย คือมีปัญหาเพราะว่าต้องส่งตัวแปรเป็น ref เพื่อให้เกิดการแก้ไขจากภายใน 
# และไม่รู้วิธีการแปลง tree ให้เป็นรูปแบบตามโจทย์ทำให้เกิดการปล่อยมันไปอย่างที่เป็น

####################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inor (r,op) :
    if r != None :
        inor(r.left,op)
        op.append(r.val)
        inor(r.right,op)
    else :
        op.append(-1)
        
def preor (r,op) :
    if r != None :
        op.append(r.val)
        preor(r.left,op)
        preor(r.right,op)
    else :
        op.append(-1)
        
def postor (r,op) :
    if r != None :
        postor(r.left,op)
        postor(r.right,op)
        op.append(r.val)
    else :
        op.append(-1)
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        _p = []
        _q = []
        inor(p,_p)
        inor(q,_q)
        if _p != _q :
            return False
        
        _p = []
        _q = []
        preor(p,_p)
        preor(q,_q)
        if _p != _q :
            return False
        
        _p = []
        _q = []
        postor(p,_p)
        postor(q,_q)
        if _p != _q :
            return False
        
        return True
       