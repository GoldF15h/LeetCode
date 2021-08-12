# ข้อนี้ไม่ปกติเพราะว่าเป็นข้อที่ ต้องใช้ตัวแปร global ทำให้เกิดปัญหาในการ ล้างตัวแปร global 
# ทำให้ไม่สามารถตอบ testcase อื่นได้ จึงต้อง passby ref

########################################################################################


def inor (c,op) :
    if c != None :
        inor(c.left,op)
        op.append(c.val)
        # print(c.val,end=' ')
        inor(c.right,op)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        op = []
        inor(root,op)
        return op

        