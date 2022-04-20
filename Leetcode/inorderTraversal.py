# Definition for a binary tree node.
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        output=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                return output
            node=stack.pop()
            output.append(node.val)
            root=node.right
        return output          

