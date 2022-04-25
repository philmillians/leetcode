# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root:
            return self.compare(root.left,root.right)
    def compare(self,leftNode,rightNode):
        if leftNode and rightNode and leftNode.val == rightNode.val:
            flag1 = self.compare(leftNode.left, rightNode.right) 
            flag2 = self.compare(leftNode.right, rightNode.left) 
            return flag1 and flag2
        elif leftNode and rightNode and leftNode.val != rightNode.val:
            return False
        elif not leftNode and rightNode:
            return False
        elif leftNode and not rightNode:
            return False
        else:
            return True
