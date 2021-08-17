class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.val)
        printTree(node.left, level + 1)

def left_rotate (node) :
    cur = node
    new_head = node.right
    cur.right = new_head.left
    new_head.left = cur
    return new_head

def right_rotate (node) :
    cur = node
    new_head = node.left
    cur.left = new_head.right
    new_head.right = cur
    return new_head
    
def height_def (node) :
    return get_tree_hight(node.left) - get_tree_hight(node.right)

def get_tree_hight (node,h=0) :
    if node != None :
        return max( get_tree_hight(node.left,h+1),get_tree_hight(node.right,h+1) )
    else :
        return h

def tree_insert (node,val) :
    if node == None :
        return TreeNode(val)
    elif node.val > val :
        node.left = tree_insert(node.left,val)
    else :
        node.right = tree_insert(node.right,val)

    d = height_def(node)

    # l l 
    if d > 1 and val < node.left.val : 
        return right_rotate(node)

    # l r
    if d > 1 and val > node.left.val : 
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # r r
    if d < -1 and val > node.right.val : 
        return left_rotate(node)

    # r l
    if d < -1 and val < node.right.val : 
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def sol (nums) :
    root = TreeNode(nums[0])
    for i in range(1,len(nums)):
        print('insert -> {}'.format(nums[i]))
        # printTree(root)
        root = tree_insert(root,nums[i])
    return root

if __name__ == "__main__" :
    l = list(map(int,input().strip('[]').split(',')))
    printTree(sol(l))