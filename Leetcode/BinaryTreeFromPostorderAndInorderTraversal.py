# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right: 
                return None
            # select the inorder_index element as the root and increment it
            value = postorder.pop()
            root = TreeNode(value)
            index = index_map[value]
            # build left and right subtree
            
            root.right = helper(index + 1, right)
            
            root.left = helper(left, index - 1)
            return root

# build a hashmap to store value -> its index relations
        index_map = {}
        for index, value in enumerate(inorder):
            index_map[value] = index

        return helper(0, len(inorder) - 1)
